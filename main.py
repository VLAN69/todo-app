from ui import ConsoleUI
from logic import TaskManager


def main():
    manager = TaskManager()
    ui = ConsoleUI(manager)
