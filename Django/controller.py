from model import TaskModel
from view import ConsoleView

class TaskController:
    def __init__(self):
        self.model = TaskModel()
        self.view = ConsoleView()

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_choice()

            if choice == "1":
                desc = self.view.get_task_description()
                if self.model.add_task(desc):
                    self.view.show_message("Завдання додано!")
                else:
                    self.view.show_message("Опис не може бути порожнім.")

            elif choice == "2":
                tasks = self.model.get_all_tasks()
                self.view.show_tasks(tasks)

            elif choice == "3":
                tasks = self.model.get_all_tasks()
                self.view.show_tasks(tasks)
                if tasks:
                    num = self.view.get_task_number("Номер завдання для позначення: ")
                    try:
                        idx = int(num) - 1
                        if self.model.mark_done(idx):
                            self.view.show_message("Завдання позначено як виконане!")
                        else:
                            self.view.show_message("Невірний номер.")
                    except ValueError:
                        self.view.show_message("Введіть число.")

            elif choice == "4":
                tasks = self.model.get_all_tasks()
                self.view.show_tasks(tasks)
                if tasks:
                    num = self.view.get_task_number("Номер завдання для видалення: ")
                    try:
                        idx = int(num) - 1
                        if self.model.delete_task(idx):
                            self.view.show_message("Завдання видалено!")
                        else:
                            self.view.show_message("Невірний номер.")
                    except ValueError:
                        self.view.show_message("Введіть число.")

            elif choice == "0":
                self.view.show_message("До побачення!")
                break

            else:
                self.view.show_message("Невірний вибір, спробуйте ще раз.")