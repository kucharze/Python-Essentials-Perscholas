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
        #For catching parsing errors and other excetions
        print(f"Error adding task: {e}")
        
def complete_task(task_list, index):
    if 0 <= index < len(task_list):
        task = task_list[index]
        task.completed = True
        print(f"Task '{task.title}' marked as completed.")
    else:
        print("Invalid task index.")
        
        
def delete_task(task_list, index):
    try:
        if 0 <= index < len(task_list):
            task = task_list.pop(index)
            print(f"Task '{task.title}' deleted.")
        else:
            print("Invalid task index.")
    except Exception as e:
        #For Catching invalid indax errors and other exceptions
        print(f"Error deleting task: {e}")