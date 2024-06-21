import datetime

""" 

Var task: 
- Beschreibung - str
- Name / Title - str
- Fälligkeitsdatum - date
- Erstelldatum - date
- Abgeschlossen j/n


"""

class task():
    def __init__(self,title:str,description:str,dueDate:datetime.date) -> None:
        self.title = title
        self.description = description
        self.dueDate = dueDate
        self.createDate = datetime.date.today()
        self.done = False
    
    
    def __str__(self) -> str:
        return f"Titel: {self.title} - Fällig am {self.dueDate} - Beschreibung: {self.description} - Abgeschlossen? {self.done}"