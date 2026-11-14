import task
import todolist
print("Welcome to the To-Do List App!")

task_list = []

while True:
    print("\nChoose an option:")
    print("A. Add a task")
    print("C. Mark a task as completed")
    print("D. Delete a task")
    print("L. List all tasks")
    print("Q. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "A":
        task = input("Enter the task: ")
        todolist.add_task(task_list, task)
        
    elif choice == "C":
        index = int(input("Enter the index of the task to mark as completed: "))
        todolist.complete_task(task_list, index)
        
    elif choice == "D":
        index = int(input("Enter the index of the task to delete: "))
        todolist.delete_task(task_list, index)
        
    elif choice == "L":
        todolist.list_tasks(task_list)
    elif choice == "Q":
        print("Exiting the To-Do List App. Goodbye!")
        break