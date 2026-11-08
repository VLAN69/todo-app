class Task:
    """Дело в списке дел."""

    def __init__(self, title: str, deadline: str, done: bool = False):
        if not title or not title.strip():
            raise ValueError("Название дела не может быть пустым")
        self.title = title.strip()
        self.deadline = deadline
        self.done = done

    def mark_done(self) -> None:
        self.done = True

    def __str__(self) -> str:
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.title} (срок: {self.deadline})"
