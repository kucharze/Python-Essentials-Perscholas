import task
import todolist
import datetime
import colorama
colorama.init()
print("Welcome to the To-Do List App!")

task_list = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
                title, due_date_str, completed_str = line.strip().split(",")
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str != "No due date" else None
                completed = completed_str == "True"
                task_obj = task.Task(title, due_date)
                task_obj.completed = completed
                task_list.append(task_obj)
except FileNotFoundError:
    print(colorama.Fore.YELLOW + "No existing task file found. Starting with an empty task list." + colorama.Style.RESET_ALL)
    

while True:
    print(colorama.Fore.CYAN + "\nChoose an option:" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "A. Add a task" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "C. Mark a task as completed" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "D. Delete a task" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "L. List all tasks" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "Q. Quit" + colorama.Style.RESET_ALL)
    
    choice = input("Enter your choice: ").upper()
    
    if choice == "A":#Add a task
        task = input("Enter the task: ")
        due_date_input = input("Enter the due date (YYYY-MM-DD) or leave blank for no due date: ")
        due_date = None
        if due_date_input != "":
            try:
                due_date = datetime.datetime.strptime(due_date_input, "%Y-%m-%d")
            except ValueError:
                print(colorama.Fore.RED + "Invalid date format. Task will be added without a due date." + colorama.Style.RESET_ALL)
                
        todolist.add_task(task_list, task, due_date)
        
    elif choice == "C":#Mark a task as completed
        index = int(input("Enter the index of the task to mark as completed: "))
        todolist.complete_task(task_list, index)
        
    elif choice == "D":#Delete a task from the list
        index = int(input("Enter the index of the task to delete: "))
        todolist.delete_task(task_list, index)
        
    elif choice == "L":#List out the tasks in the list
        todolist.list_tasks(task_list)
        
    elif choice == "Q":#Quit the application
        print(colorama.Fore.GREEN + "Exiting application. Goodbye!" + colorama.Style.RESET_ALL)
        break
    
    else:
        print(colorama.Fore.RED + "Invalid choice. Please try again." + colorama.Style.RESET_ALL)

save_tasks = input("Would you like to save your tasks to a file? (Y/N): ").upper()
if save_tasks.upper() == "Y":
    try:
        #save the tasks to a file
        with open("tasks.txt", "w") as file:
            for task in task_list:
                due_date_str = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
                file.write(f"{task.title},{due_date_str},{task.completed}\n")
                
    except IOError as e:
        print(colorama.Fore.RED + f"An error occurred while saving the file: {e}" + colorama.Style.RESET_ALL)