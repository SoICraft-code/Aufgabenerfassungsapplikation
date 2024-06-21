import unittest
from unittest.mock import patch
import datetime
from task_manager import TaskManager
from task import task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    @patch('builtins.input', side_effect=["Test Title", "Test Description", "31-12-2023"])
    def test_create_task(self, mock_input):
        new_task = self.manager.createTask()
        
        self.assertEqual(len(self.manager.allTasks), 1)
        self.assertEqual(new_task.title, "Test Title")
        self.assertEqual(new_task.description, "Test Description")
        self.assertEqual(new_task.dueDate, datetime.date(2023, 12, 31))

    def test_get_task(self):
        t = task("Test Title", "Test Description", datetime.date(2023, 12, 31))
        self.manager.allTasks.append(t)

        found_task = self.manager.getTask("Test Title")
        self.assertEqual(found_task, t)

    def test_get_all_tasks(self):
        t1 = task("Test Title 1", "Test Description 1", datetime.date(2023, 12, 31))
        t2 = task("Test Title 2", "Test Description 2", datetime.date(2024, 1, 1))
        self.manager.allTasks.extend([t1, t2])

        tasks = self.manager.getAllTasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn(t1, tasks)
        self.assertIn(t2, tasks)

    @patch('builtins.input', side_effect=[
        "Test Title",         
        "0", "Test Title Updated", 
        "1", "Test Description Updated", 
        "2", "01-01-2024", 
        "3", "j", 
        "4"  
    ])
    def test_update_task(self, mock_input):
        t = task("Test Title", "Test Description", datetime.date(2023, 12, 31))
        self.manager.allTasks.append(t)
        
        updated_task = self.manager.updateTask("Test Title")
        self.assertEqual(updated_task.title, "Test Title Updated")
        self.assertEqual(updated_task.description, "Test Description Updated")
        self.assertEqual(updated_task.dueDate, datetime.date(2024, 1, 1))
        self.assertTrue(updated_task.done)

    def test_delete_task(self):
        t = task("Test Title", "Test Description", datetime.date(2023, 12, 31))
        self.manager.allTasks.append(t)

        deleted = self.manager.deleteTask("Test Title")
        self.assertTrue(deleted)
        self.assertEqual(len(self.manager.allTasks), 0)

if __name__ == '__main__':
    unittest.main()
