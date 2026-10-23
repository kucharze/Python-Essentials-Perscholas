import task
import datetime

def add_task(task_list, title, due_date=None):
    try:
        task = task.Task(title, due_date)
        task_list.append(task)
        if due_date:
            due_date = due_date.strftime("%Y-%m-%d")
            print(f"Task '{title}' added with due date {due_date}.")
        else:
            print(f"Task '{title}' added without a due date.")
    except Exception as e:
        print(f"Error adding task: {e}")