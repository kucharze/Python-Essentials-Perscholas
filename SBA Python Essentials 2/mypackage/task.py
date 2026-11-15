class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed
        
        
    def __str__(self):
        return f"Task: {self.title}, Due Date: {self.due_date}, Completed: {self.completed}"