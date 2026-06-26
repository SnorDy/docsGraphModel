"""
Documentation Knowledge Graph Builder — CLI

Interactive command-line interface for building a Stack-Overflow-backed
knowledge graph from either:
  1. A full local project (walks .md and .java files, respects priorities)
  2. A single documentation file (.md)

Run:
    python cli.py
"""

import asyncio
import os
import sys

from StackOverflowClient import StackOverflowClient
from Graph import Graph
from ProjectAnalyzer import ProjectAnalyzer
from DocumentationAnalyzer import DocumentationAnalyzer


def ask_choice(prompt: str, options: dict) -> str:
    """
    Ask the user to pick one of several options.
    `options` maps a short key (e.g. '1') to a display label.
    Returns the chosen key.
    """
    print(f"\n{prompt}")
    for key, label in options.items():
        print(f"  [{key}] {label}")

    while True:
        choice = input("> ").strip()
        if choice in options:
            return choice
        print(f"Please enter one of: {', '.join(options.keys())}")


def ask_path(prompt: str, must_exist: bool = True, is_dir: bool = False) -> str:
    """Ask the user for a filesystem path, validating it exists (file or dir)."""
    while True:
        path = input(f"{prompt}\n> ").strip().strip('"').strip("'")
        if not path:
            print("Path cannot be empty.")
            continue
        path = os.path.expanduser(path)

        if not must_exist:
            return path

        if is_dir and not os.path.isdir(path):
            print(f"'{path}' is not a valid directory. Try again.")
            continue
        if not is_dir and not os.path.isfile(path):
            print(f"'{path}' is not a valid file. Try again.")
            continue

        return path


def ask_text(prompt: str, default: str = "") -> str:
    """Ask for a free-text value, falling back to a default if left blank."""
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}\n> ").strip()
    return value if value else default


def ask_int(prompt: str, default: int) -> int:
    """Ask for an integer value, falling back to a default if left blank or invalid."""
    raw = input(f"{prompt} [{default}]\n> ").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        print(f"Not a valid number, using default ({default}).")
        return default


def ask_api_key() -> str:
    """Ask for a Stack Exchange API key (optional — can be left blank)."""
    raw = input(
        "Stack Exchange API key (optional, press Enter to skip)\n> "
    ).strip()
    return raw or None



async def run_cli() -> None:
    print("=" * 60)
    print("  Documentation Knowledge Graph Builder")
    print("=" * 60)

    mode = ask_choice(
        "What would you like to analyze?",
        {
            "1": "A full project (scans .md and .java files, respects priorities)",
            "2": "A single documentation file (.md)",
        },
    )

    if mode == "1":
        target_path = ask_path(
            "Enter the path to the local project directory:",
            must_exist=True, is_dir=True,
        )
    else:
        target_path = ask_path(
            "Enter the path to the markdown documentation file:",
            must_exist=True, is_dir=False,
        )

    project_name = ask_text(
        "Project/framework name (used as a Stack Overflow search tag, "
        "leave blank for none)",
        default="",
    )

    api_key = ask_api_key()

    print("\n--- Graph-building parameters (press Enter to accept defaults) ---")
    max_functions = ask_int("Max number of functions to process", default=10)
    max_depth = ask_int("Max recursion depth", default=2)
    questions_per_depth = ask_int("Questions to fetch per function", default=1)
    answers_per_question = ask_int("Top answers to fetch per question", default=2)
    min_answer_score = ask_int("Minimum answer score to keep", default=2)

    output_graph_path = ask_text(
        "Output path for the graph JSON file", default="documentation_graph.json"
    )
    output_snippets_dir = ask_text(
        "Output directory for extracted code snippets", default="code_snippets"
    )

    client = StackOverflowClient(api_key=api_key, rate_limit_delay=1.5)
    graph = Graph(name="Documentation Knowledge Graph")

    try:
        print("\nExtracting functions...\n")

        if mode == "1":
            analyzer = ProjectAnalyzer(client)
            function_entries = analyzer.extract_functions_from_project(target_path)
        else:
            analyzer = DocumentationAnalyzer(client, language="java")
            function_entries = analyzer.extract_functions_from_md(target_path)
            total = len(function_entries)
            high = sum(1 for f in function_entries if f['priority'] == 'high')
            low = sum(1 for f in function_entries if f['priority'] == 'low')
            print(f"Extracted functions: {total} "
                  f"(high: {high}, normal: {total - high - low}, low: {low})")

        if not function_entries:
            print("\nNo functions were found to process. Exiting.")
            return

        function_entries = function_entries[:max_functions]
        print(f"\nProcessing top {len(function_entries)} functions (priority-sorted)\n")

        root_questions = await client.build_graph_from_documentation(
            function_entries=function_entries,
            project=project_name,
            graph=graph,
            max_depth=max_depth,
            min_answer_score=min_answer_score,
            questions_per_depth=questions_per_depth,
            answers_per_question=answers_per_question,
        )

        if not root_questions:
            print("Failed to build graph for any function. No output was generated.")
            return

        print("\n" + "=" * 50)
        print("GRAPH BUILT SUCCESSFULLY!")
        print("=" * 50)

        stats = graph.get_statistics()
        print(f"\nGraph statistics:")
        print(f"  Total nodes:    {stats['total_nodes']}")
        print(f"  Questions:      {stats['questions']}")
        print(f"  Answers:        {stats['answers']}")
        print(f"  Total edges:    {stats['total_edges']}")
        print(f"  Code snippets:  {stats['total_code_snippets']}")
        if stats['snippets_by_language']:
            print(f"  Languages:      {stats['snippets_by_language']}")

        print(f"\nRoot questions (found {len(root_questions)}):")
        for i, q in enumerate(root_questions[:5]):
            priority_label = f" [{q.extraction_priority}]" if q.extraction_priority else ""
            print(f"  {i + 1}. {q.title[:80]}...{priority_label} (score: {q.score})")
            print(f"     URL: {q.url}")

        graph.export_to_json(output_graph_path)
        print(f"\nGraph exported to: {output_graph_path}")

        snippets_summary = graph.export_code_snippets(output_snippets_dir)
        print(f"\nSnippets export summary:")
        print(f"  Files written:   {snippets_summary['files_written']}")
        print(f"  Total snippets:  {snippets_summary['total_snippets']}")
        print(f"  Index:           {snippets_summary['index_path']}")

        graph.print_tree()

    finally:
        await client.close()


def main() -> None:
    try:
        asyncio.run(run_cli())
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting.")
        sys.exit(1)


if __name__ == "__main__":
    main()
