import re
from typing import List, Optional
from Graph import Graph, Node
from StackOverflowClient import StackOverflowClient


class DocumentationAnalyzer:
    FILE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.html', '.htm', '.css', '.js', '.json', '.xml', '.txt', '.md',
                       '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.zip', '.tar', '.gz', '.svg', '.ico',
                       '.woff', '.ttf', '.eot'}

    def __init__(self, client: StackOverflowClient):
        self.client = client

    def _is_file_extension(self, name: str) -> bool:
        name_lower = name.lower()
        return any(name_lower.endswith(ext) for ext in self.FILE_EXTENSIONS)

    def extract_functions_from_md(self, file_path: str) -> List[str]:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        functions = set()

        code_blocks = re.findall(r'```(?:\w+)?\n(.*?)\n```', content, re.DOTALL)
        for block in code_blocks:
            matches = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\s*\(', block)
            functions.update(matches)
            matches = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', block)
            functions.update(matches)

        inline_code = re.findall(r'`([^`]+)`', content)
        for code in inline_code:
            matches = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code)
            functions.update(matches)
            matches = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code)
            functions.update(matches)

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