import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMainIntegration(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1', 'Task 1', 'Beschreibung 1', '15-06-2024',  # create task
        '2',  # display all tasks
        '3', 'Task 1',  # display specific task
        '4', 'Task 1', '0', 'Updated Task 1', '4',  # update task
        '5', 'Updated Task 1',  # delete task
        '6'  # exit
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_integration(self, mock_stdout, mock_input):
        # Wir erwarten keinen SystemExit, sondern das Programm soll durch die Eingabe "6" beendet werden.
        main.main()  # Keine Begrenzung der Schleifeniteration

        output = mock_stdout.getvalue()
        
        # Check the output
        self.assertIn("Aufgabe hinzufügen", output)
        self.assertIn("Alle Aufgaben anzeigen", output)
        self.assertIn("eine bestimmte Aufgabe anzeigen", output)
        self.assertIn("eine Aufgabe überarbeiten", output)
        self.assertIn("eine Aufgabe löschen", output)
        self.assertIn("Programm beenden", output)

        # Check task creation
        self.assertIn("Task 1", output)
        self.assertIn("Beschreibung 1", output)
        self.assertIn("Fällig am 2024-06-15", output)
        
        # Check task display
        self.assertIn("Titel: Task 1", output)
        self.assertIn("Beschreibung: Beschreibung 1", output)

        # Check task update
        self.assertIn("Titel: Updated Task 1", output)

        # Check task deletion
        self.assertIn("Aufgabe gelöscht!", output)

if __name__ == '__main__':
    unittest.main()
