import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMainIntegration(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1', 'Task 1', 'Beschreibung 1', '15-06-2024',  
        '2', 
        '3', 'Task 1',  
        '4', 'Task 1', '0', 'Updated Task 1', '4', 
        '5', 'Updated Task 1',  
        '6'  
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_integration(self, mock_stdout, mock_input):
        main.main()  

        output = mock_stdout.getvalue()
        
        # Ausgabe überprüfen
        self.assertIn("Aufgabe hinzufügen", output)
        self.assertIn("Alle Aufgaben anzeigen", output)
        self.assertIn("eine bestimmte Aufgabe anzeigen", output)
        self.assertIn("eine Aufgabe überarbeiten", output)
        self.assertIn("eine Aufgabe löschen", output)
        self.assertIn("Programm beenden", output)

        self.assertIn("Task 1", output)
        self.assertIn("Beschreibung 1", output)
        self.assertIn("Fällig am 2024-06-15", output)
        
        self.assertIn("Titel: Task 1", output)
        self.assertIn("Beschreibung: Beschreibung 1", output)

        self.assertIn("Titel: Updated Task 1", output)

        self.assertIn("Aufgabe gelöscht!", output)

if __name__ == '__main__':
    unittest.main()
