from typing import List, Set
import re

try:
    import tree_sitter_java
    from tree_sitter import Language, Parser
    TREESITTER_AVAILABLE = True
except ImportError:
    TREESITTER_AVAILABLE = False

class JavaFunctionExtractor:

    def __init__(self):
        if not TREESITTER_AVAILABLE:
            raise RuntimeError(
                "tree-sitter is not installed. "
                "Run: pip install tree-sitter tree-sitter-java"
            )
        java_language = Language(tree_sitter_java.language())
        self._parser = Parser(java_language)

        # Queries for the node types we care about
        self._method_query = java_language.query("""
            (method_invocation
                object: (_) @object
                name: (identifier) @method)

            (object_creation_expression
                type: (type_identifier) @class)

            (import_declaration
                (scoped_identifier) @import)
        """)

    def extract(self, code: str) -> List[str]:
        tree = self._parser.parse(code.encode('utf-8'))
        captures = self._method_query.captures(tree.root_node)

        results: Set[str] = set()

        # captures is a dict: {capture_name: [Node, ...]}
        # Handle method_invocation: combine object + method
        methods = captures.get('method', [])

        for method_node in methods:
            method_name = method_node.text.decode('utf-8')
            # find the sibling object node — it shares the same parent
            parent = method_node.parent
            if parent:
                obj_node = parent.child_by_field_name('object')
                if obj_node:
                    obj_text = obj_node.text.decode('utf-8')
                    # strip generic noise like "foo<Bar>" → "foo"
                    obj_text = re.sub(r'<[^>]+>', '', obj_text).strip()
                    results.add(f"{obj_text}.{method_name}")
                else:
                    results.add(method_name)

        # Handle object creation: new Foo() → "Foo"
        for node in captures.get('class', []):
            results.add(node.text.decode('utf-8'))

        # Handle imports: last segment and full path
        for node in captures.get('import', []):
            full = node.text.decode('utf-8')
            results.add(full)
            last = full.split('.')[-1]
            if last and not last[0].islower():  # keep only class-like names
                results.add(last)

        return sorted(results)