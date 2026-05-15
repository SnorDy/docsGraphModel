import asyncio
import html
import re
from typing import Optional, Dict, List, Set

import aiohttp

from Graph import Graph, Node, NodeType, CodeSnippet

# Maximum concurrent HTTP requests to the SO API
_MAX_CONCURRENT_REQUESTS = 5


class StackOverflowClient:
    def __init__(self, api_key: Optional[str] = None, rate_limit_delay: float = 0.5,
                 compress_bodies: bool = True):
        self.api_key = api_key
        self.base_url = "https://api.stackexchange.com/2.3"
        self.rate_limit_delay = rate_limit_delay
        self.compress_bodies = compress_bodies

        self.processed_functions: Set[str] = set()
        self.project_functions: Dict[str, Set[str]] = {}

        self.file_extensions = {
            '.png', '.jpg', '.jpeg', '.gif', '.html', '.htm', '.css', '.js', '.json', '.xml',
            '.txt', '.md', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.zip',
            '.tar', '.gz', '.svg', '.ico', '.woff', '.ttf', '.eot'
        }
        self.common_functions: Set[str] = {
            'print', 'len', 'str', 'int', 'float', 'list', 'dict', 'set', 'tuple',
            'range', 'enumerate', 'zip', 'map', 'filter', 'reduce', 'sorted',
            'min', 'max', 'sum', 'any', 'all', 'isinstance', 'hasattr', 'getattr',
            'open', 'read', 'write', 'close', 'append', 'extend', 'insert', 'remove',
            'pop', 'clear', 'copy', 'count', 'index', 'reverse', 'sort', 'join',
            'split', 'strip', 'replace', 'format', 'upper', 'lower', 'startswith',
            'endswith', 'find', 'isalpha', 'isdigit', 'isalnum'
        }
        self._LANG_ALIASES: Dict[str, str] = {
            'py': 'python', 'python3': 'python', 'python2': 'python',
            'js': 'javascript', 'ts': 'typescript',
            'sh': 'bash', 'shell': 'bash', 'zsh': 'bash',
            'rb': 'ruby',
            'cs': 'csharp', 'c#': 'csharp',
            'c++': 'cpp', 'cc': 'cpp',
            'yml': 'yaml',
        }

        # Limits concurrent HTTP requests
        self._semaphore: Optional[asyncio.Semaphore] = None
        # Serialises the rate-limit delay across all coroutines
        self._rate_lock: Optional[asyncio.Lock] = None
        self._last_request_time: float = 0.0
        # One shared aiohttp session per client
        self._session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self) -> None:
        """Close the aiohttp session. Call at the end of the program."""
        if self._session and not self._session.closed:
            await self._session.close()

    def _ensure_async_primitives(self) -> None:
        """Initialise semaphore and lock lazily (must run inside an event loop)."""
        if self._semaphore is None:
            self._semaphore = asyncio.Semaphore(_MAX_CONCURRENT_REQUESTS)
        if self._rate_lock is None:
            self._rate_lock = asyncio.Lock()

    async def _make_request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        self._ensure_async_primitives()

        if self.api_key:
            params['key'] = self.api_key
        if 'site' not in params:
            params['site'] = 'stackoverflow'

        url = f"{self.base_url}/{endpoint}"
        session = await self._get_session()

        async with self._semaphore:
            # Enforce global rate limit: only one coroutine adjusts the clock at a time
            async with self._rate_lock:
                loop = asyncio.get_event_loop()
                elapsed = loop.time() - self._last_request_time
                if elapsed < self.rate_limit_delay:
                    await asyncio.sleep(self.rate_limit_delay - elapsed)
                self._last_request_time = loop.time()

            try:
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        return await response.json()
                    print(f"API error: {response.status}")
                    return None
            except Exception as e:
                print(f"Request exception: {e}")
                return None

    async def search_questions(self, search_text: str, project: Optional[str] = None,
                               min_answers: int = 1, pagesize: int = 10) -> List[Dict]:
        params = {
            'order': 'desc', 'sort': 'relevance',
            'q': search_text, 'answers': min_answers,
            'pagesize': pagesize, 'filter': 'withbody',
        }
        if project:
            params['tagged'] = project
        data = await self._make_request('search/advanced', params)
        return data['items'] if data and 'items' in data else []

    async def get_answers_for_question(self, question_id: int, min_score: int = 0,
                                       sort_by: str = 'votes', pagesize: int = 10) -> List[Dict]:
        params = {
            'order': 'desc', 'sort': sort_by,
            'pagesize': pagesize, 'filter': 'withbody',
        }
        data = await self._make_request(f'questions/{question_id}/answers', params)
        if data and 'items' in data:
            answers = data['items']
            return [a for a in answers if a.get('score', 0) >= min_score] if min_score > 0 else answers
        return []

    async def get_best_answers(self, question_id: int, top_k: int = 3,
                               min_score: int = 0) -> List[Dict]:
        answers = await self.get_answers_for_question(question_id, min_score=min_score)
        answers.sort(key=lambda x: x.get('score', 0), reverse=True)
        return answers[:top_k]

    async def build_graph_from_function(
            self,
            function_name: str,
            project: str,
            graph: Graph,
            depth: int = 0,
            max_depth: int = 2,
            min_answer_score: int = 5,
            questions_per_depth: int = 5,
            answers_per_question: int = 3,
            parent_node_id: Optional[str] = None,
            parent_node_type: Optional[NodeType] = None,
            extraction_priority: Optional[str] = None,
    ) -> List[Node]:

        if depth > max_depth:
            return []

        func_key = f"{function_name}_{project}"
        if func_key in self.processed_functions:
            print(f"{'  ' * depth}[Depth {depth}] {function_name} already processed, skipping")
            return []
        self.processed_functions.add(func_key)

        search_text = f"{project} {function_name}".strip()
        print(f"\n{'  ' * depth}[Depth {depth}] Searching: {search_text}")

        questions = await self.search_questions(
            search_text, project=None, min_answers=1, pagesize=questions_per_depth
        )
        if not questions:
            print(f"{'  ' * depth}  Nothing found")
            return []

        questions.sort(key=lambda x: x.get('score', 0), reverse=True)
        questions = questions[:questions_per_depth]
        print(f"{'  ' * depth}  Found questions: {len(questions)}")

        added_questions: List[Node] = []

        for idx, question in enumerate(questions):
            question_id = question['question_id']
            question_node_id = f"q_{question_id}"

            if question_node_id in graph.nodes:
                print(f"{'  ' * depth}  Question {idx + 1} already in graph, skipping")
                continue

            top_answers = await self.get_best_answers(
                question_id, top_k=answers_per_question, min_score=min_answer_score
            )
            if not top_answers:
                print(f"{'  ' * depth}  Question {idx + 1}: no good answers, skipping")
                continue

            print(f"{'  ' * depth}  Question {idx + 1}: "
                  f"'{question['title'][:50]}...' (score: {question['score']})")

            question_node = Node(
                node_id=question_node_id,
                node_type=NodeType.QUESTION,
                title=question.get('title', ''),
                url=question.get('link', ''),
                score=question.get('score', 0),
                tags=question.get('tags', []),
                created_date=question.get('creation_date'),
                parent_id=parent_node_id,
                parent_type=parent_node_type,
                depth=depth,
                extraction_source=function_name,
                extraction_priority=extraction_priority,
            )
            question_body = question.get('body', '')[:5000]
            question_node.set_body(question_body, compress=self.compress_bodies)
            question_node.key_fragments = self._extract_key_fragments(question_body)
            question_node.code_snippets = self._extract_code_snippets(
                question_body, question_node_id, NodeType.QUESTION
            )
            if question_node.code_snippets:
                print(f"{'  ' * depth}    → {len(question_node.code_snippets)} snippet(s) in question")

            graph.add_node(question_node)
            added_questions.append(question_node)

            # Process all answers for this question concurrently
            await asyncio.gather(*[
                self._process_answer(
                    answer, question_node_id, project, graph, depth,
                    max_depth, min_answer_score, questions_per_depth,
                    answers_per_question, function_name,
                )
                for answer in top_answers
            ])

        return added_questions

    async def _process_answer(
            self,
            answer: Dict,
            question_node_id: str,
            project: str,
            graph: Graph,
            depth: int,
            max_depth: int,
            min_answer_score: int,
            questions_per_depth: int,
            answers_per_question: int,
            original_function: str,
    ) -> None:
        answer_node_id = f"a_{answer['answer_id']}"
        if answer_node_id in graph.nodes:
            return

        answer_node = Node(
            node_id=answer_node_id,
            node_type=NodeType.ANSWER,
            url=answer.get('link', ''),
            score=answer.get('score', 0),
            is_accepted=answer.get('is_accepted', False),
            parent_id=question_node_id,
            parent_type=NodeType.QUESTION,
            depth=depth + 1,
        )
        answer_body = answer.get('body', '')[:8000]
        answer_node.set_body(answer_body, compress=self.compress_bodies)
        answer_node.key_fragments = self._extract_key_fragments(answer_body)
        answer_node.code_snippets = self._extract_code_snippets(
            answer_body, answer_node_id, NodeType.ANSWER
        )
        graph.add_node(answer_node)
        graph.add_edge(question_node_id, answer_node_id, 'has_answer')

        snippets_info = f", {len(answer_node.code_snippets)} snippet(s)" if answer_node.code_snippets else ""
        print(f"{'  ' * depth}    Answer: score {answer.get('score', 0)}{snippets_info}")

        # Recurse into functions extracted from this answer — concurrently
        extracted = self._extract_functions_from_text(
            answer_body, project=project, original_function=original_function
        )
        recurse_tasks = [
            self.build_graph_from_function(
                func, project, graph,
                depth + 1, max_depth, min_answer_score,
                questions_per_depth, answers_per_question,
                parent_node_id=answer_node_id,
                parent_node_type=NodeType.ANSWER,
            )
            for func in extracted[:2]
            if func and func != original_function
        ]
        if recurse_tasks:
            await asyncio.gather(*recurse_tasks)

    async def build_graph_from_documentation(
            self,
            function_entries: List[Dict],
            project: str,
            graph: Graph,
            **client_kwargs,
    ) -> List[Node]:
        """
        Process all functions from documentation concurrently.
        function_entries: [{'name': str, 'priority': str|None}]
        sorted high → normal → low by DocumentationAnalyzer.
        """
        results = await asyncio.gather(*[
            self.build_graph_from_function(
                function_name=entry['name'],
                project=project,
                graph=graph,
                extraction_priority=entry['priority'],
                **client_kwargs,
            )
            for entry in function_entries
        ])
        return [node for sublist in results for node in sublist]

    def _normalize_language(self, raw: str) -> str:
        cleaned = raw.strip().lower().lstrip('language-')
        return self._LANG_ALIASES.get(cleaned, cleaned) if cleaned else 'unknown'

    def _extract_code_snippets(self, text: str, node_id: str,
                               node_type: NodeType) -> List[CodeSnippet]:
        if not text:
            return []
        snippets: List[CodeSnippet] = []
        seen_codes: Set[str] = set()
        source = node_type.value

        for match in re.finditer(
            r'<pre[^>]*>\s*<code([^>]*)>(.*?)</code>\s*</pre>', text,
            re.DOTALL | re.IGNORECASE
        ):
            attrs, raw_code = match.group(1), match.group(2)
            lang = 'unknown'
            cm = re.search(r'class=["\']([^"\']+)["\']', attrs)
            if cm:
                for cls in cm.group(1).split():
                    c = self._normalize_language(cls)
                    if c and c != 'unknown':
                        lang = c
                        break
            code = html.unescape(raw_code).strip()
            if not code or code in seen_codes or len(code) < 10:
                continue
            seen_codes.add(code)
            snippets.append(CodeSnippet(
                language=lang, code=code, source=source,
                node_id=node_id, snippet_index=len(snippets),
            ))

        if not snippets:
            for match in re.finditer(r'```([^\n`]*)\n(.*?)(?:\n```|$)', text, re.DOTALL):
                lang = self._normalize_language(match.group(1).strip()) if match.group(1).strip() else 'unknown'
                code = match.group(2).strip()
                if not code or code in seen_codes or len(code) < 10:
                    continue
                seen_codes.add(code)
                snippets.append(CodeSnippet(
                    language=lang, code=code, source=source,
                    node_id=node_id, snippet_index=len(snippets),
                ))
        return snippets

    def load_project_functions_from_docs(self, project: str, doc_functions: List[str]) -> None:
        if project not in self.project_functions:
            self.project_functions[project] = set()
        for func in doc_functions:
            clean = re.sub(r'[()]', '', func).strip()
            if len(clean) > 2:
                self.project_functions[project].add(clean)
        print(f"Loaded {len(self.project_functions[project])} functions for project {project}")

    def _extract_functions_from_text(self, text: str, project: Optional[str] = None,
                                     original_function: Optional[str] = None) -> List[str]:
        if not text:
            return []
        functions = set()
        for pattern in [r'```?\n(.*?)\n```', r'`([^`]+)`']:
            for code in re.findall(pattern, text, re.DOTALL):
                for cp in [
                    r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\s*\(',
                    r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(',
                ]:
                    for m in re.findall(cp, code):
                        if self._is_relevant_function(m.strip(), project, original_function):
                            functions.add(m.strip())
        if not functions:
            for pattern in [
                r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\b',
                r'`([a-zA-Z_][a-zA-Z0-9_]*\(\)?)`',
            ]:
                for m in re.findall(pattern, text):
                    clean = m.replace('()', '').strip()
                    if self._is_relevant_function(clean, project, original_function):
                        functions.add(clean)
        return sorted(functions, key=lambda f: (
            0 if project and f.startswith(project.lower()) else 1,
            0 if '.' in f else 1,
            -len(f),
        ))

    def _is_relevant_function(self, function_name: str, project: Optional[str],
                               original_function: Optional[str]) -> bool:
        if not function_name or len(function_name) < 3:
            return False
        if function_name.lower() in self.common_functions:
            return False
        if any(function_name.lower().endswith(ext) for ext in self.file_extensions):
            return False
        if project and project in self.project_functions and self.project_functions[project]:
            if function_name in self.project_functions[project]:
                return True
            if project.lower() in function_name.lower():
                return True
        if original_function:
            prefix = original_function.split('.')[0]
            if prefix and prefix in function_name:
                return True
        if '.' in function_name:
            if function_name.split('.')[-1] in {'toString', 'equals', 'hashCode', 'getClass', 'clone', 'finalize'}:
                return False
            return True
        return False

    def _extract_key_fragments(self, text: str, max_fragments: int = 3) -> List[str]:
        if not text:
            return []
        fragments = []
        for sentence in re.split(r'[.!?]+', text):
            sentence = sentence.strip()
            if len(sentence) < 20 or len(sentence) > 300:
                continue
            for pattern in [r'`[^`]+`',
                             r'\b(import|from|class|def|function|method|use|using|need|problem|error|issue|solution)\b']:
                if re.search(pattern, sentence, re.IGNORECASE):
                    fragments.append(sentence[:200])
                    break
            if len(fragments) >= max_fragments:
                break
        return fragments

    def reset_processed_functions(self) -> None:
        self.processed_functions.clear()