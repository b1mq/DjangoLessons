# view.py
class ConsoleView:
    @staticmethod
    def show_tasks(tasks: list["Task"]):
        if not tasks:
            print("\nСписок завдань порожній.\n")
            return

        print("\nСписок завдань:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

    @staticmethod
    def show_menu():
        print("Меню To-Do List:")
        print("  1   — Додати завдання")
        print("  2   — Показати всі завдання")
        print("  3   — Позначити як виконане")
        print("  4   — Видалити завдання")
        print("  0   — Вихід")
        print()

    @staticmethod
    def get_choice() -> str:
        return input("Виберіть дію (0-4): ").strip()

    @staticmethod
    def get_task_description() -> str:
        return input("Введіть опис завдання: ").strip()

    @staticmethod
    def get_task_number(prompt: str) -> str:
        return input(prompt).strip()

    @staticmethod
    def show_message(msg: str):
        print(f"\n{msg}\n")