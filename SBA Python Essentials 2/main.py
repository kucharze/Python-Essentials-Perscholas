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
        task_list.append({"title": task, "completed": False})
    elif choice == "Q":
        print("Exiting the To-Do List App. Goodbye!")
        break