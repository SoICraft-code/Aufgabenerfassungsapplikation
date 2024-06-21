import unittest
import datetime
from task import task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        title = "Test Title"
        description = "Test Description"
        dueDate = datetime.date(2023, 12, 31)
        t = task(title, description, dueDate)

        self.assertEqual(t.title, title)
        self.assertEqual(t.description, description)
        self.assertEqual(t.dueDate, dueDate)
        self.assertEqual(t.createDate, datetime.date.today())
        self.assertFalse(t.done)

    def test_task_str(self):
        title = "Test Title"
        description = "Test Description"
        dueDate = datetime.date(2023, 12, 31)
        t = task(title, description, dueDate)

        expected_str = f"Titel: {title} - Fällig am {dueDate} - Beschreibung: {description} - Abgeschlossen? False"
        self.assertEqual(str(t), expected_str)

if __name__ == '__main__':
    unittest.main()
