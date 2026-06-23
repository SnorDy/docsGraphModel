from typing import List, Set, Dict, Optional
import re

try:
    import tree_sitter_java
    from tree_sitter import Language, Parser, Query, QueryCursor
    TREESITTER_AVAILABLE = True
except ImportError:
    TREESITTER_AVAILABLE = False

# Priority constants — shared convention with DocumentationAnalyzer
PRIORITY_HIGH = 'high'
PRIORITY_LOW = 'low'
PRIORITY_NONE = None

# Matches // priority: high   or   // priority: low   (single-line Java comment)
_PRIORITY_COMMENT_RE = re.compile(r'//\s*priority\s*:\s*(high|low)\s*$', re.IGNORECASE)


class JavaFunctionExtractor:
    """
    Extracts Java function/method references using TreeSitter.

    Two extraction modes:
      - extract(code):              function/method *calls* and references
                                     found in arbitrary code snippets (e.g.
                                     fenced code blocks inside markdown docs).
      - extract_definitions(code):  function/method/class *definitions* found
                                     in a full Java source file, each tagged
                                     with a priority if a `// priority: high/low`
                                     comment immediately precedes it.
    """

    def __init__(self):
        if not TREESITTER_AVAILABLE:
            raise RuntimeError(
                "tree-sitter is not installed. "
                "Run: pip install tree-sitter tree-sitter-java"
            )
        java_language = Language(tree_sitter_java.language())
        self._parser = Parser(java_language)

        # Query for calls / references (used for markdown code-block extraction)
        self._method_query = Query(java_language, """
            (method_invocation
                object: (_) @object
                name: (identifier) @method)

            (object_creation_expression
                type: (type_identifier) @class)

            (import_declaration
                (scoped_identifier) @import)
        """)
        self._method_cursor = QueryCursor(self._method_query)

        # Query for definitions (used for full source-file extraction)
        self._definition_query = Query(java_language, """
            (method_declaration
                name: (identifier) @method_def) @method_node

            (constructor_declaration
                name: (identifier) @ctor_def) @ctor_node

            (class_declaration
                name: (identifier) @class_def) @class_node

            (interface_declaration
                name: (identifier) @interface_def) @interface_node
        """)
        self._definition_cursor = QueryCursor(self._definition_query)


    def extract(self, code: str) -> List[str]:
        """Extract method calls, object creations, and imports from a code snippet."""
        tree = self._parser.parse(code.encode('utf-8'))
        captures = self._method_cursor.captures(tree.root_node)

        results: Set[str] = set()

        methods = captures.get('method', [])
        for method_node in methods:
            method_name = method_node.text.decode('utf-8')
            parent = method_node.parent
            if parent:
                obj_node = parent.child_by_field_name('object')
                if obj_node:
                    obj_text = obj_node.text.decode('utf-8')
                    obj_text = re.sub(r'<[^>]+>', '', obj_text).strip()
                    results.add(f"{obj_text}.{method_name}")
                else:
                    results.add(method_name)

        for node in captures.get('class', []):
            results.add(node.text.decode('utf-8'))

        for node in captures.get('import', []):
            full = node.text.decode('utf-8')
            results.add(full)
            last = full.split('.')[-1]
            if last and not last[0].islower():
                results.add(last)

        return sorted(results)

    def extract_definitions(self, code: str) -> List[Dict[str, Optional[str]]]:
        """
        Extract method, constructor, class, and interface DEFINITIONS from a
        full Java source file.

        A definition's priority is set if a `// priority: high` or
        `// priority: low` comment appears immediately above it (allowing for
        blank lines and other comment lines in between, as long as there is
        no other code statement between the comment and the definition).

        Returns a list of dicts: {'name': str, 'priority': 'high'|'low'|None}
        """
        tree = self._parser.parse(code.encode('utf-8'))
        captures = self._definition_cursor.captures(tree.root_node)

        definitions: List[Dict[str, Optional[str]]] = []
        seen_node_ids: Set[int] = set()

        def_pairs = [
            ('method_node', 'method_def'),
            ('ctor_node', 'ctor_def'),
            ('class_node', 'class_def'),
            ('interface_node', 'interface_def'),
        ]

        for node_key, name_key in def_pairs:
            decl_nodes = captures.get(node_key, [])
            name_nodes = captures.get(name_key, [])
            name_by_start = {n.start_byte: n for n in name_nodes}

            for decl_node in decl_nodes:
                if decl_node.id in seen_node_ids:
                    continue
                seen_node_ids.add(decl_node.id)

                name_node = None
                for start, n in name_by_start.items():
                    if decl_node.start_byte <= start < decl_node.end_byte:
                        name_node = n
                        break
                if name_node is None:
                    continue

                name = name_node.text.decode('utf-8')
                priority = self._find_priority_above(code, decl_node)
                definitions.append({'name': name, 'priority': priority})

        # Deduplicate by name (e.g. class + its same-named constructor),
        # keeping the best priority found for that name
        order = {'high': 0, None: 1, 'low': 2}
        best: Dict[str, Optional[str]] = {}
        for d in definitions:
            name, prio = d['name'], d['priority']
            if name not in best or order[prio] < order[best[name]]:
                best[name] = prio

        return [{'name': name, 'priority': prio} for name, prio in best.items()]

    def _find_priority_above(self, code: str, decl_node) -> Optional[str]:
        """
        Look for a `// priority: high/low` comment that precedes a
        declaration. TreeSitter's declaration node span starts at the first
        modifier/annotation (e.g. `@Override`), not at the `public` keyword,
        so a priority comment sitting between annotations and the keyword
        falls *inside* the node span rather than strictly above it.

        To handle this, we scan from the start of the declaration's own
        source text forward through any leading annotation/comment lines,
        then also scan backward from the declaration's start_byte through
        blank lines, comments, and annotations in the surrounding source.
        Whichever priority comment is found nearest to the actual keyword
        (`public`/`class`/`private`/etc.) wins.
        """
        decl_start = decl_node.start_byte
        decl_end = decl_node.end_byte
        decl_text = code[decl_start:decl_end]

        # 1) Look inside the declaration's own text, before the first
        #    non-comment/non-annotation/non-blank line (covers the case
        #    where the comment sits between annotations and the keyword).
        decl_lines = decl_text.split('\n')
        for line in decl_lines:
            stripped = line.strip()
            if not stripped:
                continue
            priority_match = _PRIORITY_COMMENT_RE.search(stripped)
            if priority_match:
                return priority_match.group(1).lower()
            if stripped.startswith('//') or stripped.startswith('*') or stripped.startswith('/*'):
                continue
            if stripped.startswith('@'):
                continue
            break  # hit the actual keyword/identifier line — stop looking inside

        # 2) Look backward from decl_start through preceding blank/comment lines
        #    (covers the case where the comment sits entirely before any
        #    annotations, e.g. directly above `@Override`).
        prefix = code[:decl_start]
        for line in reversed(prefix.split('\n')):
            stripped = line.strip()
            if not stripped:
                continue
            priority_match = _PRIORITY_COMMENT_RE.search(stripped)
            if priority_match:
                return priority_match.group(1).lower()
            if stripped.startswith('//') or stripped.startswith('*') or stripped.startswith('/*'):
                continue
            if stripped.startswith('@'):
                continue
            break  # hit actual code — stop, no priority comment applies here

        return None
