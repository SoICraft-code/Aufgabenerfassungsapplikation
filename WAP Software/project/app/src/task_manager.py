""" 
Funktionen des Systems
- Aufgaben erstellen: Hinzufügen neuer Aufgaben mit Titel, Beschreibung und Fälligkeitsdatum.
- Aufgaben anzeigen: Auflisten aller Aufgaben oder Anzeigen einer einzelnen Aufgabe.
- Aufgaben aktualisieren: Bearbeiten bestehender Aufgaben.
- Aufgaben löschen: Entfernen von Aufgaben aus der Liste.

"""

from task import *


class TaskManager():
    def __init__(self) -> None:
        self.allTasks = []
    
    def createTask(self)-> task:
        title = input("Bitte geben Sie einen Titel ein!\n Titel: ")
        desc = input("Bitte geben Sie eine Beschreibung ein!\n Beschreibung: ")
        while True:
            try:
                date = input("Bitte geben Sie ein Fälligkeitsdatum ein!\n Datum: ")
                date = date.split("-")
                date = datetime.date(int(date[2]),int(date[1]),int(date[0]))
                break
            except ValueError or TypeError:
                print("Bitte geben Sie ein gültiges Datum ein!")
        newTask = task(title=title,description=desc,dueDate=date)
        self.allTasks.append(newTask)
        return newTask
    
    def getTask(self,title:str) -> task:
        for i in range(len(self.allTasks)):
            if self.allTasks[i].title == title:
                return self.allTasks[i]
        return False
        
    def getAllTasks(self) -> list:
        return self.allTasks
            
    def updateTask(self,title:str) -> task:
        task = self.getTask(title)
        if task:
            while True:
                print("Bitte geben Sie an was Sie bearbeiten wollen:")
                print("0 - Titel")
                print("1 - Beschreibung")
                print("2 - Fälligkeitsdatum")
                print("3 - Status")
                print("4 - Beenden")
                uInput = input("\n Eingabe: ")
                if(uInput == "0"):
                    newTitle = input("Bitte geben Sie den Neuen Titel ein!")
                    task.title = newTitle
                    
                elif(uInput == "1"):
                    newDesc = input("Bitte geben Sie die neue Beschreibung ein!")
                    task.description = newDesc
                    
                elif(uInput == "2"):
                    while True:
                        try:
                            date = input("Bitte geben Sie ein neues Fälligkeitsdatum an!\n Datum: ")
                            date = date.split("-")
                            date = datetime.date(int(date[2]),int(date[1]),int(date[0]))
                            break
                        except ValueError or TypeError:
                            print("Bitte geben Sie ein gültiges Datum ein!")
                    
                    task.dueDate = date
                    
                elif(uInput == "3"):
                    while True:
                        done = input("Ist die Aufgabe abgeschlossen? j/n")
                        if done == "j" or done == "n":
                            if done == "j":
                                task.done = True
                            else: 
                                task.done = False
                            break
                        else:
                            print("Bitte geben Sie eine gültige Eingabe ein!")
                    
                elif( uInput == "4"):
                    break
                else:
                    print("Bitte eine gültige Eingabe Tätigen!")
        return task
  
    def deleteTask(self,title:str) -> bool:
        task = self.getTask(title)
        if task:
            for i in self.allTasks:
                if i == task:
                    self.allTasks.pop(self.allTasks.index(task))
                    break
            return True
        return False
            
    