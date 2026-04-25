import json
import zlib
import base64
from typing import List, Dict, Optional, Set
from dataclasses import dataclass, field
from enum import Enum
import os


class NodeType(Enum):
    QUESTION = "question"
    ANSWER = "answer"


def compress_text(text: str, compress: bool = True) -> str:
    if not compress or not text:
        return text

    compressed = zlib.compress(text.encode('utf-8'))
    return base64.b64encode(compressed).decode('ascii')


def decompress_text(compressed_text: str) -> str:
    if not compressed_text:
        return ""

    try:
        decoded = base64.b64decode(compressed_text.encode('ascii'))
        decompressed = zlib.decompress(decoded)
        return decompressed.decode('utf-8')
    except:
        return compressed_text


@dataclass
class CodeSnippet:
    """A single code snippet extracted from a Stack Overflow post."""
    language: str          # e.g. "python", "javascript", "unknown"
    code: str              # raw code text
    source: str            # "question" or "answer"
    node_id: str           # parent node id
    snippet_index: int     # position among snippets in this node (0-based)

    def to_dict(self) -> Dict:
        return {
            'language': self.language,
            'code': self.code,
            'source': self.source,
            'node_id': self.node_id,
            'snippet_index': self.snippet_index,
        }


@dataclass
class Node:
    node_id: str
    node_type: NodeType

    title: Optional[str] = None
    body: str = ""
    body_compressed: bool = False
    url: str = ""
    score: int = 0

    tags: List[str] = field(default_factory=list)
    created_date: Optional[int] = None
    is_accepted: bool = False
    parent_id: Optional[str] = None
    parent_type: Optional[NodeType] = None
    depth: int = 0
    extraction_source: Optional[str] = None
    key_fragments: List[str] = field(default_factory=list)
    code_snippets: List[CodeSnippet] = field(default_factory=list)

    def __hash__(self):
        return hash(self.node_id)

    def __eq__(self, other):
        return self.node_id == other.node_id

    def is_question(self) -> bool:
        return self.node_type == NodeType.QUESTION

    def is_answer(self) -> bool:
        return self.node_type == NodeType.ANSWER

    def get_body(self, decompress: bool = True) -> str:
        if decompress and self.body_compressed:
            return decompress_text(self.body)
        return self.body

    def set_body(self, body: str, compress: bool = True) -> None:
        if compress and len(body) > 500:
            self.body = compress_text(body)
            self.body_compressed = True
        else:
            self.body = body
            self.body_compressed = False

    def to_dict(self) -> Dict:
        result = {
            'node_id': self.node_id,
            'node_type': self.node_type.value if isinstance(self.node_type, NodeType) else self.node_type,
            'body_preview': self.get_body(decompress=False)[:200] + '...' if len(
                self.get_body(decompress=False)) > 200 else self.get_body(decompress=False),
            'body_length': len(self.get_body(decompress=False)),
            'body_compressed': self.body_compressed,
            'key_fragments': self.key_fragments,
            'code_snippets': [s.to_dict() for s in self.code_snippets],
            'code_snippets_count': len(self.code_snippets),
            'url': self.url,
            'score': self.score,
            'depth': self.depth,
            'parent_id': self.parent_id,
            'parent_type': self.parent_type.value if self.parent_type and isinstance(self.parent_type,
                                                                                     NodeType) else self.parent_type,
        }

        if self.is_question():
            result['title'] = self.title
            result['tags'] = self.tags
            result['created_date'] = self.created_date
        else:
            result['is_accepted'] = self.is_accepted

        if self.extraction_source:
            result['extraction_source'] = self.extraction_source

        return result


@dataclass
class Edge:
    from_node_id: str
    to_node_id: str
    edge_type: str

    def __hash__(self):
        return hash((self.from_node_id, self.to_node_id, self.edge_type))

    def to_dict(self) -> Dict:
        return {
            'from': self.from_node_id,
            'to': self.to_node_id,
            'type': self.edge_type
        }


class Graph:
    def __init__(self, name: str = "StackOverflowGraph", compress_bodies: bool = True):
        self.name = name
        self.compress_bodies = compress_bodies
        self.nodes: Dict[str, Node] = {}
        self.edges: Set[Edge] = set()

        self._questions: Dict[str, Node] = {}
        self._answers: Dict[str, Node] = {}
        self._children_by_parent: Dict[str, List[str]] = {}
        self._links_from_answer: Dict[str, List[str]] = {}
        self._backlinks_to_question: Dict[str, List[str]] = {}

    def add_node(self, node: Node) -> None:
        if node.node_id in self.nodes:
            return

        self.nodes[node.node_id] = node

        if node.is_question():
            self._questions[node.node_id] = node
        else:
            self._answers[node.node_id] = node

        if node.parent_id:
            if node.parent_id not in self._children_by_parent:
                self._children_by_parent[node.parent_id] = []
            self._children_by_parent[node.parent_id].append(node.node_id)

    def add_edge(self, from_id: str, to_id: str, edge_type: str) -> bool:
        if from_id not in self.nodes or to_id not in self.nodes:
            print(f"Failed to add edge {from_id} -> {to_id}: nodes do not exist")
            return False

        edge = Edge(from_id, to_id, edge_type)
        self.edges.add(edge)

        if edge_type == 'contains_link_to_question':
            if from_id not in self._links_from_answer:
                self._links_from_answer[from_id] = []
            self._links_from_answer[from_id].append(to_id)

            if to_id not in self._backlinks_to_question:
                self._backlinks_to_question[to_id] = []
            self._backlinks_to_question[to_id].append(from_id)

            question_node = self.nodes[to_id]
            if question_node.parent_id is None:
                question_node.parent_id = from_id
                question_node.parent_type = self.nodes[from_id].node_type

        elif edge_type == 'has_answer':
            answer_node = self.nodes[to_id]
            if answer_node.parent_id is None:
                answer_node.parent_id = from_id
                answer_node.parent_type = self.nodes[from_id].node_type

        return True

    def get_children(self, node_id: str) -> List[Node]:
        child_ids = self._children_by_parent.get(node_id, [])
        return [self.nodes[c_id] for c_id in child_ids if c_id in self.nodes]

    def get_parent(self, node_id: str) -> Optional[Node]:
        node = self.nodes.get(node_id)
        if node and node.parent_id and node.parent_id in self.nodes:
            return self.nodes[node.parent_id]
        return None

    def get_question_answers(self, question_id: str) -> List[Node]:
        children = self.get_children(question_id)
        return [c for c in children if c.is_answer()]

    def get_links_from_answer(self, answer_id: str) -> List[Node]:
        children = self.get_children(answer_id)
        return [c for c in children if c.is_question()]

    def get_backlinks_to_question(self, question_id: str) -> List[Node]:
        answer_ids = self._backlinks_to_question.get(question_id, [])
        return [self.nodes[a_id] for a_id in answer_ids if a_id in self.nodes]

    def get_root_nodes(self) -> List[Node]:
        return [node for node in self.nodes.values() if node.parent_id is None]

    def get_statistics(self) -> Dict:
        edge_types = {}
        for edge in self.edges:
            edge_types[edge.edge_type] = edge_types.get(edge.edge_type, 0) + 1

        depth_distribution = {}
        total_compressed_size = 0
        total_uncompressed_size = 0
        total_snippets = 0
        snippets_by_language: Dict[str, int] = {}

        for node in self.nodes.values():
            depth_distribution[node.depth] = depth_distribution.get(node.depth, 0) + 1
            body = node.get_body(decompress=False)
            total_compressed_size += len(body) if node.body_compressed else len(node.body)
            total_uncompressed_size += len(node.get_body(decompress=True))

            total_snippets += len(node.code_snippets)
            for snippet in node.code_snippets:
                lang = snippet.language or 'unknown'
                snippets_by_language[lang] = snippets_by_language.get(lang, 0) + 1

        return {
            'total_nodes': len(self.nodes),
            'questions': len(self._questions),
            'answers': len(self._answers),
            'total_edges': len(self.edges),
            'edge_types': edge_types,
            'root_nodes': len(self.get_root_nodes()),
            'depth_distribution': depth_distribution,
            'avg_children_per_node': (
                sum(len(children) for children in self._children_by_parent.values()) / len(self.nodes)
                if self.nodes else 0
            ),
            'compression_ratio': f"{total_compressed_size}/{total_uncompressed_size} ({100 - (total_compressed_size / total_uncompressed_size * 100) if total_uncompressed_size > 0 else 0:.1f}% saved)",
            'total_code_snippets': total_snippets,
            'snippets_by_language': snippets_by_language,
        }

    def print_tree(self, node_id: str = None, max_depth: int = 3, prefix: str = "", is_last: bool = True):
        if node_id is None:
            roots = self.get_root_nodes()
            for i, root in enumerate(roots[:5]):
                is_last_root = (i == len(roots[:5]) - 1)
                self.print_tree(root.node_id, max_depth, "", is_last_root)
                if not is_last_root:
                    print()
            return

        if max_depth < 0:
            return

        node = self.nodes.get(node_id)
        if not node:
            return

        connector = "└── " if is_last else "├── "

        if node.is_question():
            snippets_info = f", snippets: {len(node.code_snippets)}" if node.code_snippets else ""
            print(f"{prefix}{connector} QUESTION: {node.title[:60]}... (score: {node.score}, depth: {node.depth}{snippets_info})")
        else:
            snippets_info = f", snippets: {len(node.code_snippets)}" if node.code_snippets else ""
            print(
                f"{prefix}{connector}ANSWER: (score: {node.score}, accepted: {node.is_accepted}, depth: {node.depth}{snippets_info})")

        new_prefix = prefix + ("    " if is_last else "│   ")
        children = self.get_children(node_id)
        for i, child in enumerate(children[:5]):
            is_last_child = (i == len(children[:5]) - 1)
            self.print_tree(child.node_id, max_depth - 1, new_prefix, is_last_child)

        if len(children) > 5:
            print(f"{new_prefix}└── ... and {len(children) - 5} more nodes")

    def export_to_json(self, filepath: str, include_full_body: bool = False) -> None:
        export_data = {
            'name': self.name,
            'statistics': self.get_statistics(),
            'nodes': {},
            'edges': [e.to_dict() for e in self.edges],
            'root_nodes': [node.node_id for node in self.get_root_nodes()]
        }

        for node_id, node in self.nodes.items():
            node_dict = node.to_dict()
            if include_full_body:
                node_dict['full_body'] = node.get_body(decompress=True)
            export_data['nodes'][node_id] = node_dict

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)

        print(f"Graph exported to {filepath}")

    def export_code_snippets(self, output_dir: str = "code_snippets") -> Dict:
        os.makedirs(output_dir, exist_ok=True)
        questions_dir = os.path.join(output_dir, "questions")
        answers_dir = os.path.join(output_dir, "answers")
        os.makedirs(questions_dir, exist_ok=True)
        os.makedirs(answers_dir, exist_ok=True)

        index_entries = []
        files_written = 0
        total_snippets = 0

        for node_id, node in self.nodes.items():
            if not node.code_snippets:
                continue

            node_data: Dict = {
                'node_id': node_id,
                'node_type': node.node_type.value,
                'url': node.url,
                'score': node.score,
                'extraction_source': node.extraction_source,
                'snippets': [
                    {
                        'snippet_index': s.snippet_index,
                        'language': s.language,
                        'code': s.code,
                    }
                    for s in node.code_snippets
                ],
            }

            if node.is_question():
                node_data['title'] = node.title
                node_data['tags'] = node.tags
                target_dir = questions_dir
            else:
                node_data['is_accepted'] = node.is_accepted
                # include parent question title for context
                parent = self.get_parent(node_id)
                if parent and parent.is_question():
                    node_data['parent_question_title'] = parent.title
                    node_data['parent_question_url'] = parent.url
                target_dir = answers_dir

            file_path = os.path.join(target_dir, f"{node_id}.json")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(node_data, f, ensure_ascii=False, indent=2)
            files_written += 1
            total_snippets += len(node.code_snippets)

            # add flat entry to index
            for snippet in node.code_snippets:
                index_entries.append({
                    'node_id': node_id,
                    'node_type': node.node_type.value,
                    'url': node.url,
                    'score': node.score,
                    'extraction_source': node.extraction_source,
                    'title': node.title if node.is_question() else None,
                    'language': snippet.language,
                    'snippet_index': snippet.snippet_index,
                    'code_preview': snippet.code[:300] + '...' if len(snippet.code) > 300 else snippet.code,
                    'file': os.path.join(
                        'questions' if node.is_question() else 'answers',
                        f"{node_id}.json"
                    ),
                })

        index_path = os.path.join(output_dir, "index.json")
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump({
                'total_snippets': total_snippets,
                'files_written': files_written,
                'snippets': index_entries,
            }, f, ensure_ascii=False, indent=2)

        summary = {
            'output_dir': output_dir,
            'files_written': files_written,
            'total_snippets': total_snippets,
            'index_path': index_path,
        }
        print(
            f"Code snippets exported: {total_snippets} snippets across "
            f"{files_written} nodes → {output_dir}/"
        )
        return summary