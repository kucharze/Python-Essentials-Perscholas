class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed