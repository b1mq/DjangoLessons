# main.py
import sys
import platform
from controller import TaskController


def set_console_title(title: str):
    """
    встановлює заголовок вікна терміналу.
    працює на Windows, macOS, Linux (більшість терміналів).
    """

    if platform.system() == "Windows":
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleTitleW(title)
            return 
        except Exception:
            pass 

    try:
        sys.stdout.write(f"\x1b]2;{title}\x1b\\")
        sys.stdout.flush()
    except Exception:
        pass


if __name__ == "__main__":
    set_console_title("Список завдань")
    app = TaskController()
    app.run()