import task
import datetime

def add_task(tasks, title, due_date=None):
    task = Task(title, due_date)
    tasks.append(task)
    print(f"Task '{title}' added.")