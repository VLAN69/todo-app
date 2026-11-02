import unittest

from logic import Task


class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task("Сделать лабораторную", "2026-11-10")
        self.assertEqual(task.title, "Сделать лабораторную")
        self.assertEqual(task.deadline, "2026-11-10")
        self.assertFalse(task.done)

    def test_create_done_task(self):
        task = Task("Сдать отчёт", "2026-11-12", done=True)
        self.assertTrue(task.done)

    def test_mark_done(self):
        task = Task("Сдать отчёт", "2026-11-12")
        task.mark_done()
        self.assertTrue(task.done)

    def test_str(self):
        task = Task("Сдать отчёт", "2026-11-12")
        self.assertEqual(str(task), "Сдать отчёт (до 2026-11-12) — не выполнено")
        task.mark_done()
        self.assertEqual(str(task), "Сдать отчёт (до 2026-11-12) — выполнено")


if __name__ == "__main__":
    unittest.main()
