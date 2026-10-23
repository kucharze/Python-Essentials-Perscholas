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
        
def complete_task(task_list, index):
    if 0 <= index < len(task_list):
        task = task_list[index]
        task.completed = True
        print(f"Task '{task.title}' marked as completed.")
    else:
        print("Invalid task index.")