from StackOverflowClient import StackOverflowClient
from Graph import Graph
from DocumentationAnalyzer import DocumentationAnalyzer

def main():
    client = StackOverflowClient(
        api_key='rl_zvtmkNchGzUAZUwEf4CttWecx',
        rate_limit_delay=1.5
    )
    graph = Graph(name="Documentation Knowledge Graph")
    analyzer = DocumentationAnalyzer(client)
    md_file = "combined.md"
    project_name = ""

    root_questions = analyzer.build_graph_from_documentation(
        md_file_path=md_file,
        project=project_name,
        graph=graph,
        max_functions=10,
        max_depth=2,
        min_answer_score=2,
        questions_per_depth=1,
        answers_per_question=2
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
            print(f"  {i+1}. {q.title[:80]}... (score: {q.score})")
            print(f"     URL: {q.url}")

        graph.export_to_json("documentation_graph.json")


        snippets_summary = graph.export_code_snippets("code_snippets")
        print(f"\nSnippets export summary:")
        print(f"  Files written:   {snippets_summary['files_written']}")
        print(f"  Total snippets:  {snippets_summary['total_snippets']}")
        print(f"  Index:           {snippets_summary['index_path']}")

        graph.print_tree()
    else:
        print("Failed to build graph for any function from the documentation")

if __name__ == "__main__":
    main()