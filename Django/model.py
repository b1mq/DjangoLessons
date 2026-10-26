# model.py
class Task:
    def __init__(self, description: str, done: bool = False):
        self.description = description
        self.done = done

    def __str__(self):
        status = "✓" if self.done else " "
        return f"[{status}] {self.description}"


class TaskModel:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, description: str):
        if description.strip():
            self.tasks.append(Task(description.strip()))
            return True
        return False

    def get_all_tasks(self) -> list[Task]:
        return self.tasks.copy() # повертаємо копію, щоб не зламати зовні

    def mark_done(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
            return True
        return False

    def delete_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False