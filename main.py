import asyncio
from StackOverflowClient import StackOverflowClient
from Graph import Graph
from ProjectAnalyzer import ProjectAnalyzer


async def main():
    client = StackOverflowClient(
        api_key='rl_zvtmkNchGzUAZUwEf4CttWecx',
        rate_limit_delay=1.5,
    )
    graph = Graph(name="Documentation Knowledge Graph")

    # Path to a local project directory (e.g. a cloned GitHub repo)
    project_path = r"C:\Users\Snordy\KotlinMKN\kotlin-2025-class7-SnorDy"
    project_name = ""

    analyzer = ProjectAnalyzer(client)

    try:
        # Step 1: walk the project, extract + prioritise functions from
        # every .md and .java file (sync, fast — no network calls here)
        function_entries = analyzer.extract_functions_from_project(project_path)

        max_functions = 10
        function_entries = function_entries[:max_functions]
        print(f"Processing top {max_functions} functions (priority-sorted)\n")

        # Step 2: build graph concurrently
        root_questions = await client.build_graph_from_documentation(
            function_entries=function_entries,
            project=project_name,
            graph=graph,
            max_depth=2,
            min_answer_score=2,
            questions_per_depth=1,
            answers_per_question=2,
        )

        if root_questions:
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
                print(f"  {i+1}. {q.title[:80]}...{priority_label} (score: {q.score})")
                print(f"     URL: {q.url}")

            graph.export_to_json("documentation_graph.json")

            snippets_summary = graph.export_code_snippets("code_snippets")
            print(f"\nSnippets export summary:")
            print(f"  Files written:   {snippets_summary['files_written']}")
            print(f"  Total snippets:  {snippets_summary['total_snippets']}")
            print(f"  Index:           {snippets_summary['index_path']}")

            graph.print_tree()
        else:
            print("Failed to build graph for any function from the project")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
