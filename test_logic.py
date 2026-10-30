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


if __name__ == "__main__":
    unittest.main()
