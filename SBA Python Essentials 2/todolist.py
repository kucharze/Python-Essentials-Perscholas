import task
import datetime
import colorama
colorama.init()

def add_task(task_list, title, due_date=None):
    try:
        taskoption = task.Task(title, due_date)
        task_list.append(taskoption)
        if due_date:
            due_date = due_date.strftime("%Y-%m-%d")
            print(f"Task '{title}' added with due date {due_date}.")
        else:
            print(f"Task '{title}' added without a due date.")
    except Exception as e:
        #For catching parsing errors and other excetions
        print(colorama.Fore.RED + f"Error adding task: {e}" + colorama.Style.RESET_ALL)
        
def complete_task(task_list, index):
    if 0 <= index < len(task_list):
        task = task_list[index]
        task.completed = True
        print(f"Task '{task.title}' marked as completed.")
    else:
        print(colorama.Fore.RED + "Invalid task index." + colorama.Style.RESET_ALL)
        
        
def delete_task(task_list, index):
    try:
        if 0 <= index < len(task_list):
            task = task_list.pop(index)
            print(f"Task '{task.title}' deleted.")
        else:
            print(colorama.Fore.RED + "Invalid task index." + colorama.Style.RESET_ALL)
    except Exception as e:
        #For Catching invalid indax errors and other exceptions
        print(colorama.Fore.RED + f"Error deleting task: {e}" + colorama.Style.RESET_ALL)


def list_tasks(task_list):
    if not task_list:
        print(colorama.Fore.YELLOW + "No tasks in the list." + colorama.Style.RESET_ALL)
        return

    for index, task in enumerate(task_list):
        status = "Completed" if task.completed else "Pending"
        due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
        
        overdue = ""
        if task.due_date and task.due_date < datetime.datetime.now():
            overdue = "(Overdue)"
            
        print(f"{index}. {task.title} - {status} - Due: {due_date} {overdue}")