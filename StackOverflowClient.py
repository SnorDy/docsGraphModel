import re
import requests
import time
from typing import Optional, Dict, List, Set
from Graph import Graph, Node, NodeType


class StackOverflowClient:
    def __init__(self, api_key: Optional[str] = None, rate_limit_delay: float = 0.5,
                 compress_bodies: bool = True):
        self.api_key = api_key
        self.base_url = "https://api.stackexchange.com/2.3"
        self.rate_limit_delay = rate_limit_delay
        self.last_request_time = 0
        self.processed_functions: Set[str] = set()
        self.compress_bodies = compress_bodies

        self.project_functions: Dict[str, Set[str]] = {}  # project -> set of functions


        self.common_functions: Set[str] = {
            'print', 'len', 'str', 'int', 'float', 'list', 'dict', 'set', 'tuple',
            'range', 'enumerate', 'zip', 'map', 'filter', 'reduce', 'sorted',
            'min', 'max', 'sum', 'any', 'all', 'isinstance', 'hasattr', 'getattr',
            'open', 'read', 'write', 'close', 'append', 'extend', 'insert', 'remove',
            'pop', 'clear', 'copy', 'count', 'index', 'reverse', 'sort', 'join',
            'split', 'strip', 'replace', 'format', 'upper', 'lower', 'startswith',
            'endswith', 'find', 'isalpha', 'isdigit', 'isalnum'
        }

    def load_project_functions_from_docs(self, project: str, doc_functions: List[str]) -> None:

        if project not in self.project_functions:
            self.project_functions[project] = set()

        for func in doc_functions:
            clean_func = re.sub(r'[()]', '', func).strip()
            if len(clean_func) > 2:
                self.project_functions[project].add(clean_func)

        print(f"Загружено {len(self.project_functions[project])} функций для проекта {project}")

    def _extract_functions_from_text(self, text: str, project: Optional[str] = None,
                                     original_function: Optional[str] = None) -> List[str]:
        if not text:
            return []

        functions = set()
        code_patterns = [
            r'```?\n(.*?)\n```',
            r'`([^`]+)`',
        ]

        for pattern in code_patterns:
            code_matches = re.findall(pattern, text, re.DOTALL)
            for code in code_matches:
                call_patterns = [
                    r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\s*\(',
                    r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(',
                ]
                for call_pattern in call_patterns:
                    matches = re.findall(call_pattern, code)
                    for match in matches:
                        clean_func = match.strip()
                        if self._is_relevant_function(clean_func, project, original_function):
                            functions.add(clean_func)

        if not functions:
            text_patterns = [
                r'\b([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\b',
                r'`([a-zA-Z_][a-zA-Z0-9_]*\(\)?)`',
            ]

            for pattern in text_patterns:
                matches = re.findall(pattern, text)
                for match in matches:
                    clean_func = match.replace('()', '').strip()
                    if self._is_relevant_function(clean_func, project, original_function):
                        functions.add(clean_func)


        sorted_functions = sorted(functions, key=lambda f: (
            0 if project and f.startswith(project.lower()) else 1,
            0 if '.' in f else 1,
            -len(f)
        ))

        return sorted_functions

    def _is_relevant_function(self, function_name: str, project: Optional[str],
                              original_function: Optional[str]) -> bool:
        if not function_name or len(function_name) < 3:
            return False

        if function_name.lower() in self.common_functions:
            return False
        if project and project in self.project_functions and self.project_functions[project]:
            if function_name in self.project_functions[project]:
                return True

            if project.lower() in function_name.lower():
                return True

        if original_function:
            original_prefix = original_function.split('.')[0]
            if original_prefix and original_prefix in function_name:
                return True

        if '.' in function_name:
            common_methods = {'toString', 'equals', 'hashCode', 'getClass', 'clone', 'finalize'}
            if function_name.split('.')[-1] in common_methods:
                return False
            return True

        return False

    def _extract_key_fragments(self, text: str, max_fragments: int = 3) -> List[str]:
        if not text:
            return []

        fragments = []

        sentences = re.split(r'[.!?]+', text)

        important_patterns = [
            r'`[^`]+`',
            r'\b(import|from|class|def|function|method|use|using|need|problem|error|issue|solution)\b',
        ]

        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 20 or len(sentence) > 300:
                continue

            for pattern in important_patterns:
                if re.search(pattern, sentence, re.IGNORECASE):
                    fragments.append(sentence[:200])
                    break

            if len(fragments) >= max_fragments:
                break

        return fragments

    def _make_request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - time_since_last)

        if self.api_key:
            params['key'] = self.api_key

        if 'site' not in params:
            params['site'] = 'stackoverflow'

        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.get(url, params=params)
            self.last_request_time = time.time()

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Ошибка API: {response.status_code}")
                return None
        except Exception as e:
            print(f"Исключение при запросе: {e}")
            return None

    def search_questions(self, search_text: str, project: Optional[str] = None,
                         min_answers: int = 1, pagesize: int = 10) -> List[Dict]:
        params = {
            'order': 'desc',
            'sort': 'relevance',
            'q': search_text,
            'answers': min_answers,
            'pagesize': pagesize,
            'filter': 'withbody'
        }

        if project:
            params['tagged'] = project

        data = self._make_request('search/advanced', params)

        if data and 'items' in data:
            return data['items']
        return []

    def get_question_by_id(self, question_id: int) -> Optional[Dict]:
        params = {'filter': 'withbody'}
        data = self._make_request(f'questions/{question_id}', params)

        if data and 'items' in data and len(data['items']) > 0:
            return data['items'][0]
        return None

    def get_answers_for_question(self, question_id: int, min_score: int = 0,
                                 sort_by: str = 'votes', pagesize: int = 10) -> List[Dict]:
        params = {
            'order': 'desc',
            'sort': sort_by,
            'pagesize': pagesize,
            'filter': 'withbody'
        }

        data = self._make_request(f'questions/{question_id}/answers', params)

        if data and 'items' in data:
            answers = data['items']
            if min_score > 0:
                answers = [a for a in answers if a.get('score', 0) >= min_score]
            return answers
        return []

    def get_best_answers(self, question_id: int, top_k: int = 3, min_score: int = 0) -> List[Dict]:
        all_answers = self.get_answers_for_question(question_id, min_score=min_score)
        all_answers.sort(key=lambda x: x.get('score', 0), reverse=True)
        return all_answers[:top_k]

    def build_graph_from_function(self, function_name: str, project: str,
                                  graph: Graph, depth: int = 0, max_depth: int = 2,
                                  min_answer_score: int = 5,
                                  questions_per_depth: int = 5,
                                  answers_per_question: int = 3,
                                  parent_node_id: Optional[str] = None,
                                  parent_node_type: Optional[NodeType] = None) -> List[Node]:

        if depth > max_depth:
            return []

        func_key = f"{function_name}_{project}"
        if func_key in self.processed_functions:
            print(f"{'  ' * depth}[Глубина {depth}] Функция {function_name} уже обрабатывалась, пропускаем")
            return []
        self.processed_functions.add(func_key)

        search_text = f"{project} {function_name}"
        print(f"\n{'  ' * depth}[Глубина {depth}] Ищем: {search_text}")

        questions = self.search_questions(search_text, project=None,
                                          min_answers=1,
                                          pagesize=questions_per_depth)

        if not questions:
            print(f"{'  ' * depth}  Ничего не найдено")
            return []

        questions.sort(key=lambda x: x.get('score', 0), reverse=True)
        questions = questions[:questions_per_depth]

        print(f"{'  ' * depth}  Найдено вопросов: {len(questions)}")

        added_questions = []

        for idx, question in enumerate(questions):
            question_id = question['question_id']
            question_node_id = f"q_{question_id}"

            if question_node_id in graph.nodes:
                print(f"{'  ' * depth}  Вопрос {idx + 1} уже есть в графе, пропускаем")
                continue

            top_answers = self.get_best_answers(question_id,
                                                top_k=answers_per_question,
                                                min_score=min_answer_score)

            if not top_answers:
                print(f"{'  ' * depth}  Вопрос {idx + 1}: нет хороших ответов, пропускаем")
                continue

            print(f"{'  ' * depth}  Вопрос {idx + 1}: '{question['title'][:50]}...' (рейтинг: {question['score']})")

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
                extraction_source=function_name
            )

            question_body = question.get('body', '')[:3000]
            question_node.set_body(question_body, compress=self.compress_bodies)
            question_node.key_fragments = self._extract_key_fragments(question_body)

            graph.add_node(question_node)
            added_questions.append(question_node)

            for ans_idx, answer in enumerate(top_answers):
                answer_id = answer['answer_id']
                answer_node_id = f"a_{answer_id}"

                if answer_node_id in graph.nodes:
                    continue

                answer_node = Node(
                    node_id=answer_node_id,
                    node_type=NodeType.ANSWER,
                    url=answer.get('link', ''),
                    score=answer.get('score', 0),
                    is_accepted=answer.get('is_accepted', False),
                    parent_id=question_node_id,
                    parent_type=NodeType.QUESTION,
                    depth=depth + 1
                )

                answer_body = answer.get('body', '')[:4000]  # Ответы могут быть длиннее
                answer_node.set_body(answer_body, compress=self.compress_bodies)
                answer_node.key_fragments = self._extract_key_fragments(answer_body)

                graph.add_node(answer_node)
                graph.add_edge(question_node_id, answer_node_id, 'has_answer')
                print(f"{'  ' * depth}    Ответ {ans_idx + 1}: рейтинг {answer.get('score', 0)}")

                extracted_functions = self._extract_functions_from_text(
                    answer_body,
                    project=project,
                    original_function=function_name
                )

                for extracted_function in extracted_functions[:2]:
                    if extracted_function and extracted_function != function_name:
                        print(f"{'  ' * depth} Найдена функция в ответе: {extracted_function}")

                        self.build_graph_from_function(
                            extracted_function, project, graph,
                            depth + 1, max_depth, min_answer_score,
                            questions_per_depth, answers_per_question,
                            parent_node_id=answer_node_id,
                            parent_node_type=NodeType.ANSWER
                        )

        return added_questions

    def reset_processed_functions(self):
        self.processed_functions.clear()