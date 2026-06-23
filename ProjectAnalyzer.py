import os
from typing import List, Dict, Optional

from DocumentationAnalyzer import DocumentationAnalyzer, PRIORITY_HIGH, PRIORITY_LOW, PRIORITY_NONE
from JavaFunctionExtractor import JavaFunctionExtractor, TREESITTER_AVAILABLE
from StackOverflowClient import StackOverflowClient

# Directories that are never useful for finding documentation or source
# definitions, and are usually huge (build artifacts, VCS metadata, deps).
DEFAULT_IGNORED_DIRS = {
    '.git', '.svn', '.hg',
    'build', 'target', 'out', 'dist',
    'node_modules', '.gradle', '.idea', '.vscode',
    '__pycache__', '.venv', 'venv',
}

# Sort key: high first, then unset, then low (mirrors DocumentationAnalyzer)
_PRIORITY_ORDER = {PRIORITY_HIGH: 0, PRIORITY_NONE: 1, PRIORITY_LOW: 2}

# File extensions handled by each analyzer
MARKDOWN_EXTENSIONS = {'.md', '.markdown'}
JAVA_EXTENSIONS = {'.java'}


class ProjectAnalyzer:
    """
    Walks a local project directory and extracts prioritised function names
    from every relevant file, dispatching to the right per-file analyzer:

      - .md / .markdown  → DocumentationAnalyzer  (mentions/calls in docs)
      - .java            → JavaFunctionExtractor   (definitions in source)

    Other file types are skipped. Results from all files are merged into a
    single priority-sorted list, ready to feed into
    StackOverflowClient.build_graph_from_documentation.
    """

    def __init__(self, client: StackOverflowClient,
                 ignored_dirs: Optional[set] = None):
        self.client = client
        self.ignored_dirs = ignored_dirs if ignored_dirs is not None else set(DEFAULT_IGNORED_DIRS)

        # Reuse a single DocumentationAnalyzer for markdown files (language="java"
        # so fenced ```java blocks inside docs use TreeSitter too)
        self._doc_analyzer = DocumentationAnalyzer(client, language="java")

        self._java_extractor: Optional[JavaFunctionExtractor] = None
        if TREESITTER_AVAILABLE:
            try:
                self._java_extractor = JavaFunctionExtractor()
            except Exception as e:
                print(f"[TreeSitter] Failed to initialise Java extractor: {e}")


    def _walk_project_files(self, root_path: str) -> List[str]:
        """Recursively collect all relevant file paths, skipping ignored dirs."""
        matched_files: List[str] = []

        for dirpath, dirnames, filenames in os.walk(root_path):
            # Prune ignored directories in-place so os.walk doesn't descend into them
            dirnames[:] = [d for d in dirnames if d not in self.ignored_dirs]

            for filename in filenames:
                ext = os.path.splitext(filename)[1].lower()
                if ext in MARKDOWN_EXTENSIONS or ext in JAVA_EXTENSIONS:
                    matched_files.append(os.path.join(dirpath, filename))

        return matched_files


    def _extract_from_markdown_file(self, file_path: str) -> List[Dict]:
        try:
            return self._doc_analyzer.extract_functions_from_md(file_path)
        except Exception as e:
            print(f"  [skip] Failed to parse markdown {file_path}: {e}")
            return []

    def _extract_from_java_file(self, file_path: str) -> List[Dict]:
        if self._java_extractor is None:
            print(f"  [skip] No Java extractor available for {file_path}")
            return []
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()
            return self._java_extractor.extract_definitions(code)
        except Exception as e:
            print(f"  [skip] Failed to parse Java file {file_path}: {e}")
            return []


    def extract_functions_from_project(self, project_path: str) -> List[Dict]:
        """
        Walk the project, extract function entries from every .md and .java
        file, merge by name (best priority wins: high > None > low), and
        return a single priority-sorted list of {'name': str, 'priority': ...}.
        """
        if not os.path.isdir(project_path):
            raise ValueError(f"Project path does not exist or is not a directory: {project_path}")

        files = self._walk_project_files(project_path)
        md_files = [f for f in files if os.path.splitext(f)[1].lower() in MARKDOWN_EXTENSIONS]
        java_files = [f for f in files if os.path.splitext(f)[1].lower() in JAVA_EXTENSIONS]

        print(f"Project scan: {len(md_files)} markdown file(s), {len(java_files)} Java file(s)")

        priority_map: Dict[str, Optional[str]] = {}

        def _merge(name: str, priority: Optional[str]) -> None:
            if name not in priority_map:
                priority_map[name] = priority
                return
            # Promote: high beats anything, None beats low
            existing = priority_map[name]
            if existing == priority:
                return
            if priority == PRIORITY_HIGH or existing == PRIORITY_HIGH:
                priority_map[name] = PRIORITY_HIGH
            elif priority == PRIORITY_NONE or existing == PRIORITY_NONE:
                priority_map[name] = PRIORITY_NONE
            # else both are 'low' — stays 'low' (already handled by equality check above)

        for md_file in md_files:
            print(f"  Parsing markdown: {md_file}")
            for entry in self._extract_from_markdown_file(md_file):
                _merge(entry['name'], entry['priority'])

        for java_file in java_files:
            print(f"  Parsing Java source: {java_file}")
            for entry in self._extract_from_java_file(java_file):
                _merge(entry['name'], entry['priority'])

        result = [{'name': name, 'priority': prio} for name, prio in priority_map.items()]
        result.sort(key=lambda x: (_PRIORITY_ORDER[x['priority']], x['name']))

        high = sum(1 for e in result if e['priority'] == PRIORITY_HIGH)
        low = sum(1 for e in result if e['priority'] == PRIORITY_LOW)
        print(f"\nTotal unique functions across project: {len(result)} "
              f"(high: {high}, normal: {len(result) - high - low}, low: {low})")

        return result
