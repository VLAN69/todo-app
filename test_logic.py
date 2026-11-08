import unittest

from logic import Task, TaskManager


class TestTask(unittest.TestCase):
    def test_mark_done(self):
        task = Task("Дело", "2025-11-01")
        self.assertFalse(task.done)
        task.mark_done()
        self.assertTrue(task.done)

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            Task("   ", "2025-11-01")

    def test_title_is_stripped(self):
        task = Task("  Купить хлеб  ", "2025-11-01")
        self.assertEqual(task.title, "Купить хлеб")

    def test_str(self):
        task = Task("Купить хлеб", "2025-11-01")
        self.assertEqual(str(task), "[ ] Купить хлеб (срок: 2025-11-01)")
        task.mark_done()
        self.assertEqual(str(task), "[x] Купить хлеб (срок: 2025-11-01)")


class TestTaskManager(unittest.TestCase):
    def test_add_and_count(self):
        m = TaskManager()
        m.add_task("Дело 1", "2025-11-01")
        m.add_task("Дело 2", "2025-11-02")
        self.assertEqual(m.count(), 2)

    def test_remove_missing_raises(self):
        m = TaskManager()
        with self.assertRaises(ValueError):
            m.remove_task("Нет такого")

    def test_remove_task(self):
        m = TaskManager()
        m.add_task("Дело", "2025-11-01")
        m.remove_task("Дело")
        self.assertEqual(m.count(), 0)

    def test_mark_done(self):
        m = TaskManager()
        m.add_task("Дело", "2025-11-01")
        m.mark_done("Дело")
        self.assertTrue(m.get_all()[0].done)

    def test_mark_done_missing_raises(self):
        m = TaskManager()
        with self.assertRaises(ValueError):
            m.mark_done("Нет такого")

    def test_get_pending(self):
        m = TaskManager()
        m.add_task("Дело 1", "2025-11-01")
        m.add_task("Дело 2", "2025-11-02")
        m.mark_done("Дело 1")
        pending = m.get_pending()
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0].title, "Дело 2")

    def test_get_all_returns_copy(self):
        m = TaskManager()
        m.add_task("Дело", "2025-11-01")
        m.get_all().clear()
        self.assertEqual(m.count(), 1)


if __name__ == "__main__":
    unittest.main()
