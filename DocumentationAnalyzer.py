from typing import List, Optional, Set
import re
from Graph import Graph, Node
from StackOverflowClient import StackOverflowClient
from JavaFunctionExtractor import JavaFunctionExtractor, TREESITTER_AVAILABLE


class DocumentationAnalyzer:
    FILE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.html', '.htm', '.css', '.js', '.json', '.xml', '.txt', '.md',
                       '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.zip', '.tar', '.gz', '.svg', '.ico',
                       '.woff', '.ttf', '.eot'}

    # Languages that map to the Java TreeSitter extractor
    JAVA_LANG_HINTS = {'java'}
    def __init__(self, client: StackOverflowClient, language: Optional[str] = None):
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

    def _get_extractor_for_lang(self, lang_hint: str) -> Optional[JavaFunctionExtractor]:
        """Return the TreeSitter extractor for a given language hint, or None."""
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

        matches = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\s*\(', text)
        functions.update(matches)
        matches = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', text)
        functions.update(matches)
        mentions = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\b', text)
        functions.update(mentions)

        return functions


    def extract_functions_from_md(self, file_path: str) -> List[str]:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        functions: Set[str] = set()

        # Fenced code blocks
        # Match ```lang\n code \n``` capturing the language hint and body
        fenced_pattern = re.compile(r'```(\w*)\n(.*?)\n```', re.DOTALL)

        for match in fenced_pattern.finditer(content):
            lang_hint = match.group(1).strip().lower()
            block_code = match.group(2)

            # Determine effective language
            effective_lang = self.language or lang_hint

            if effective_lang and self._get_extractor_for_lang(effective_lang):
                # TreeSitter path
                extracted = self._extract_functions_treesitter(block_code, effective_lang)
                functions.update(extracted)
            else:
                # Regex fallback for this block
                functions.update(self._extract_functions_regex(block_code))

        # Inline code  `foo()`
        for inline in re.findall(r'`([^`]+)`', content):
            functions.update(self._extract_functions_regex(inline))

        # Plain text mentions  obj.method
        mentions = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\b', content)
        functions.update(mentions)

        common_words = {'the', 'and', 'for', 'with', 'this', 'that', 'have', 'from',
                        'are', 'was', 'were', 'been', 'has', 'had', 'will', 'would',
                        'could', 'should', 'may', 'might', 'what', 'when', 'where',
                        'which', 'while', 'using', 'your', 'more', 'other', 'some'}

        filtered = []
        for f in functions:
            if len(f) < 3:
                continue
            if f.isdigit():
                continue
            if f.lower() in common_words:
                continue
            if self._is_file_extension(f):
                continue
            filtered.append(f)

        return sorted(set(filtered))



    def build_graph_from_documentation(self, md_file_path: str, project: str,
                                       graph: Graph,
                                       max_functions: Optional[int] = None,
                                       **client_kwargs) -> List[Node]:
        functions = self.extract_functions_from_md(md_file_path)
        print(f"Extracted functions from documentation: {len(functions)}")
        if max_functions:
            functions = functions[:max_functions]
            print(f"Limited to {max_functions} functions for processing")

        all_root_questions = []
        for func in functions:
            print(f"\n--- Processing function: {func} ---")
            root_questions = self.client.build_graph_from_function(
                function_name=func,
                project=project,
                graph=graph,
                **client_kwargs
            )
            if root_questions:
                all_root_questions.extend(root_questions)

        return all_root_questions