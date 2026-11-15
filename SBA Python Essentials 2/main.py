from mypackage import task
from mypackage import todolist
import datetime
print("Welcome to the To-Do List App!")

task_list = []

with open("tasks.txt", "r") as file:
    for line in file:
        title, due_date_str, completed_str = line.strip().split(",")
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
        completed = completed_str == "True"
        task_obj = task.Task(title, due_date)
        task_obj.completed = completed
        task_list.append(task_obj)
        

while True:
    print("\nChoose an option:")
    print("A. Add a task")
    print("C. Mark a task as completed")
    print("D. Delete a task")
    print("L. List all tasks")
    print("Q. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "A":#Add a task
        task = input("Enter the task: ")
        todolist.add_task(task_list, task)
        
    elif choice == "C":#Mark a task as completed
        index = int(input("Enter the index of the task to mark as completed: "))
        todolist.complete_task(task_list, index)
        
    elif choice == "D":#Delete a task from the list
        index = int(input("Enter the index of the task to delete: "))
        todolist.delete_task(task_list, index)
        
    elif choice == "L":#List out the tasks in the list
        todolist.list_tasks(task_list)
        
    elif choice == "Q":#Quit the application
        print("Exiting application. Goodbye!")
        break
    
    
    else:
        print("Invalid choice. Please try again.")
        
#save the tasks to a file
with open("tasks.txt", "w") as file:
    for task in task_list:
        due_date_str = task.due_date.strftime("%Y-%m-%d") if task.due_date else ""
        file.write(f"{task.title},{due_date_str},{task.completed}\n")