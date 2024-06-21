from task_manager import TaskManager

def main():
    manager = TaskManager()
    while True:
       

        print("\n")
        print("1. Aufgabe hinzufügen")
        print("2. Alle Aufgaben anzeigen")
        print("3. eine bestimmte Aufgabe anzeigen")
        print("4. eine Aufgabe überarbeiten")
        print("5. eine Aufgabe löschen ")
        print("6. Programm beenden")
        choice = input("Auswahl: ")

        if choice == '1':
            print(manager.createTask())
        elif choice == '2':
            tasks = manager.getAllTasks()
            for task in tasks:
                print(task) 
        elif choice == '3':
            title = input("Geben Sie den Titel der Aufgabe an: ")
            task = manager.getTask(title)
            if task:
                print(task)
            else:
                print("Aufgabe nicht gefunden!")
        elif choice == '4':
            title = input("Geben Sie den Titel der Aufgabe an: ")
            taskn = manager.updateTask(title)
            if taskn:
                print(taskn)
            else:
                print("Aufgabe nicht gefunden!")
        elif choice == '5':
            title = input("Geben Sie den Titel der Aufgabe an: ")
            deleted_task = manager.deleteTask(title)
            if deleted_task:
                print("Aufgabe gelöscht!")
            else:
                print("Aufgabe nicht gefunden!")
        elif choice == '6':
            break
        else:
            print("ungültige Eingabe")

if __name__ == "__main__":
    main()
