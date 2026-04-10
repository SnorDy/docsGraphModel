from StackOverflowClient import  StackOverflowClient
from Graph import *

def main():
    client = StackOverflowClient(api_key='rl_zvtmkNchGzUAZUwEf4CttWecx',rate_limit_delay=1.5)

    graph = Graph(name="Example Graph")

    root_questions = client.build_graph_from_function(
        function_name="sort",
        project="python",
        graph=graph,
        max_depth=2,
        min_answer_score=2,
        questions_per_depth=1,
        answers_per_question=2
    )

    if root_questions:
        print("\n" + "=" * 50)
        print("ГРАФ ПОСТРОЕН УСПЕШНО!")
        print("=" * 50)

        stats = graph.get_statistics()
        print(f"\nСтатистика графа:")
        print(f"  Всего узлов: {stats['total_nodes']}")
        print(f"  Вопросов: {stats['questions']}")
        print(f"  Ответов: {stats['answers']}")
        print(f"  Всего связей: {stats['total_edges']}")

        print(f"\nКорневые вопросы (найдено {len(root_questions)}):")
        for i, q in enumerate(root_questions[:3]):
            print(f"  {i + 1}. {q.title[:80]}... (рейтинг: {q.score})")
            print(f"     Ссылка: {q.url}")
        graph.export_to_json("stackoverflow_graph.json")
        graph.print_tree()

    else:
        print("Не удалось построить граф для указанной функции")


if __name__ == "__main__":
    main()