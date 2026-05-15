from typing import List, Optional, Set, Dict, Tuple
import re
from Graph import Graph, Node
from StackOverflowClient import StackOverflowClient
from JavaFunctionExtractor import JavaFunctionExtractor, TREESITTER_AVAILABLE

# Priority constants
PRIORITY_HIGH = 'high'
PRIORITY_LOW = 'low'
PRIORITY_NONE = None

# Sort key: high first, then unset, then low
_PRIORITY_ORDER = {PRIORITY_HIGH: 0, PRIORITY_NONE: 1, PRIORITY_LOW: 2}


class DocumentationAnalyzer:
    FILE_EXTENSIONS = {
        '.png', '.jpg', '.jpeg', '.gif', '.html', '.htm', '.css', '.js', '.json', '.xml', '.txt', '.md',
        '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.zip', '.tar', '.gz', '.svg', '.ico',
        '.woff', '.ttf', '.eot', '.com', '.github', '.http', '.google', '.org', '.amazon'
    }

    JAVA_LANG_HINTS = {'java'}

    # Matches <!-- priority: high --> or <!-- priority: low -->
    _PRIORITY_COMMENT_RE = re.compile(
        r'<!--\s*priority\s*:\s*(high|low)\s*-->', re.IGNORECASE
    )
    # Fenced code block:  ```lang\n...\n```
    _FENCED_BLOCK_RE = re.compile(r'```(\w*)\n(.*?)\n```', re.DOTALL)
    # Inline code: `foo()`
    _INLINE_CODE_RE = re.compile(r'`([^`]+)`')
    # Plain dotted mentions: obj.method
    _DOTTED_MENTION_RE = re.compile(r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\b')

    _COMMON_WORDS = {
        'the', 'and', 'for', 'with', 'this', 'that', 'have', 'from',
        'are', 'was', 'were', 'been', 'has', 'had', 'will', 'would',
        'could', 'should', 'may', 'might', 'what', 'when', 'where',
        'which', 'while', 'using', 'your', 'more', 'other', 'some',
    }

    def __init__(self, client: StackOverflowClient, language: Optional[str] = None):
        """
        Args:
            client:   StackOverflowClient instance.
            language: Target language for TreeSitter parsing, e.g. "java".
                      If None, language is inferred from fenced code block hints.
        """
        self.client = client
        self.language = language.lower().strip() if language else None
        self._java_extractor: Optional[JavaFunctionExtractor] = None

        if TREESITTER_AVAILABLE:
            try:
                self._java_extractor = JavaFunctionExtractor()
            except Exception as e:
                print(f"[TreeSitter] Failed to initialise Java extractor: {e}")


    def _is_file_extension(self, name: str) -> bool:
        name_lower = name.lower()
        return any(name_lower.endswith(ext) for ext in self.FILE_EXTENSIONS)

    def _is_noise(self, name: str) -> bool:
        if len(name) < 3:
            return True
        if name.isdigit():
            return True
        if name.lower() in self._COMMON_WORDS:
            return True
        if self._is_file_extension(name):
            return True
        return False

    def _get_extractor_for_lang(self, lang_hint: str) -> Optional[JavaFunctionExtractor]:
        lang = lang_hint.lower().strip()
        if lang in self.JAVA_LANG_HINTS and self._java_extractor:
            return self._java_extractor
        return None

    def _extract_functions_treesitter(self, code: str, lang: str) -> List[str]:
        extractor = self._get_extractor_for_lang(lang)
        if extractor is None:
            return []
        try:
            return extractor.extract(code)
        except Exception as e:
            print(f"[TreeSitter] Parse error ({lang}), falling back to regex: {e}")
            return []

    def _extract_functions_regex(self, text: str) -> Set[str]:
        functions = set()
        functions.update(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\s*\(', text))
        functions.update(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', text))
        functions.update(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\b', text))
        return functions

    def _extract_from_text(self, text: str, lang: str = '') -> Set[str]:
        """Extract functions from a code block or plain text, choosing backend by language."""
        effective_lang = self.language or lang
        if effective_lang and self._get_extractor_for_lang(effective_lang):
            results = self._extract_functions_treesitter(text, effective_lang)
            return set(results)
        return self._extract_functions_regex(text)


    def _parse_blocks(self, content: str) -> List[Tuple[str, Optional[str]]]:
        """
        Split markdown content into (text_chunk, priority) pairs.

        A <!-- priority: high/low --> comment attaches its priority to the
        *next* block (fenced code, inline code, or plain-text paragraph).
        A block with no preceding priority comment gets priority=None.

        Returns a flat list of (chunk_text, priority) tuples where each chunk
        is either a fenced code body, an inline code snippet, or a plain-text
        paragraph.
        """
        blocks: List[Tuple[str, Optional[str]]] = []

        # We'll scan through the document position by position, tracking the
        # most recently seen priority comment that hasn't been consumed yet.
        pending_priority: Optional[str] = None
        cursor = 0
        n = len(content)

        # Build a merged list of all interesting spans sorted by start position:
        #   - priority comments
        #   - fenced code blocks
        #   - inline code
        # We process them in order and attach pending priority to the next non-comment span.

        spans = []

        for m in self._PRIORITY_COMMENT_RE.finditer(content):
            spans.append(('priority', m.start(), m.end(), m.group(1).lower(), m))

        for m in self._FENCED_BLOCK_RE.finditer(content):
            spans.append(('fenced', m.start(), m.end(), m.group(1), m))

        for m in self._INLINE_CODE_RE.finditer(content):
            # Skip if this inline code is inside a fenced block
            spans.append(('inline', m.start(), m.end(), '', m))

        # Sort by position
        spans.sort(key=lambda x: x[1])

        # Remove inline spans that fall inside fenced blocks
        fenced_ranges = [
            (m.start(), m.end())
            for kind, s, e, _, m in spans
            if kind == 'fenced'
        ]

        def inside_fenced(start: int) -> bool:
            return any(fs <= start < fe for fs, fe in fenced_ranges)

        pending_priority = None
        for kind, start, end, extra, match in spans:
            if kind == 'priority':
                pending_priority = extra  # 'high' or 'low'
                continue

            if kind == 'fenced':
                lang_hint = extra
                code_body = match.group(2)
                blocks.append((code_body, pending_priority, lang_hint))
                pending_priority = None

            elif kind == 'inline':
                if inside_fenced(start):
                    continue
                blocks.append((match.group(1), pending_priority, ''))
                pending_priority = None

        # Also handle plain-text paragraphs that follow a priority comment.
        # We do a second pass for priority comments whose pending_priority was
        # never consumed (i.e., no code block followed them directly — just prose).
        # Re-scan: find priority comments and grab the text until the next
        # comment or code block.
        code_and_comment_re = re.compile(
            r'(?:<!--\s*priority\s*:\s*(?:high|low)\s*-->|```[\s\S]*?```)',
            re.IGNORECASE
        )
        parts = code_and_comment_re.split(content)
        delimiters = code_and_comment_re.findall(content)

        pending_priority = None
        for i, delim in enumerate(delimiters):
            priority_match = self._PRIORITY_COMMENT_RE.match(delim)
            if priority_match:
                # The text that follows (parts[i+1]) is a plain-text paragraph
                # — but only add it if the pending wasn't already consumed by
                # a code block above.
                following_text = parts[i + 1] if i + 1 < len(parts) else ''
                # Check if there's a fenced/inline block at the start of following_text
                first_fenced = self._FENCED_BLOCK_RE.search(following_text)
                first_inline = self._INLINE_CODE_RE.search(following_text)
                has_code_immediately = (first_fenced and first_fenced.start() < 80) or \
                                       (first_inline and first_inline.start() < 80)
                if not has_code_immediately and following_text.strip():
                    # Plain text paragraph — take first 500 chars
                    blocks.append((following_text[:500], priority_match.group(1).lower(), ''))

        return blocks  # list of (text, priority, lang_hint)

    def extract_functions_from_md(self, file_path: str) -> List[Dict]:
        """
        Parse a markdown file and return a list of dicts:
            {'name': str, 'priority': 'high' | 'low' | None}
        sorted by priority (high → none → low), then alphabetically.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        priority_map: Dict[str, Optional[str]] = {}

        def _update(name: str, priority: Optional[str]) -> None:
            if self._is_noise(name):
                return
            existing = priority_map.get(name, PRIORITY_LOW)
            # Promote priority: high > None > low
            if existing is None and priority == PRIORITY_HIGH:
                priority_map[name] = PRIORITY_HIGH
            elif existing == PRIORITY_LOW and priority in (PRIORITY_HIGH, PRIORITY_NONE):
                priority_map[name] = priority
            elif name not in priority_map:
                priority_map[name] = priority

        blocks = self._parse_blocks(content)
        for text, priority, lang_hint in blocks:
            extracted = self._extract_from_text(text, lang_hint)
            for name in extracted:
                _update(name, priority)

        # Also pick up plain dotted mentions from full content (no priority)
        for name in self._DOTTED_MENTION_RE.findall(content):
            if name not in priority_map:
                _update(name, PRIORITY_NONE)

        # Build sorted result list
        result = [
            {'name': name, 'priority': prio}
            for name, prio in priority_map.items()
        ]
        result.sort(key=lambda x: (_PRIORITY_ORDER[x['priority']], x['name']))

        return result

    def build_graph_from_documentation(self, md_file_path: str, project: str,
                                       graph: Graph,
                                       max_functions: Optional[int] = None,
                                       **client_kwargs) -> List[Node]:
        function_entries = self.extract_functions_from_md(md_file_path)

        total = len(function_entries)
        high_count = sum(1 for f in function_entries if f['priority'] == PRIORITY_HIGH)
        low_count  = sum(1 for f in function_entries if f['priority'] == PRIORITY_LOW)
        none_count = total - high_count - low_count

        print(f"Extracted functions from documentation: {total} "
              f"(high: {high_count}, normal: {none_count}, low: {low_count})")

        if max_functions:
            function_entries = function_entries[:max_functions]
            print(f"Limited to {max_functions} functions for processing "
                  f"(after priority sort — high-priority functions are first)")

        all_root_questions = []
        for entry in function_entries:
            func_name = entry['name']
            priority  = entry['priority']
            print(f"\n--- Processing function: {func_name} "
                  f"[priority: {priority or 'normal'}] ---")

            root_questions = self.client.build_graph_from_function(
                function_name=func_name,
                project=project,
                graph=graph,
                extraction_priority=priority,
                **client_kwargs
            )
            if root_questions:
                all_root_questions.extend(root_questions)

        return all_root_questions