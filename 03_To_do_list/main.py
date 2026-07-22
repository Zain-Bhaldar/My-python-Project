#Empty list to add task
to_do_list = []
#Function to add a task
def add_task():
    task = input("Enter the task: ")
    to_do_list.append({"task": task, "Status": "pending"})
    print("Task added successfully!\n")

#Function to view tasks
def view_tasks():  

    print("To-Do List:")
    if len(to_do_list) == 0:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(to_do_list, 1):
            print(f"{index}: {task['task']} - {task['Status']}")
    print("/n")

#Function to remove a task
def remove_task():
    view_tasks()
    if len(to_do_list) == 0:
        return
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(to_do_list):
        removed_task = to_do_list.pop(task_index)
        print(f"Task '{removed_task['task']}' removed successfully!\n")
    else:
        print("Invalid task number. Please try again.\n")

#Function to mark a task as completed
def mark_task_completed():
    view_tasks()
    if len(to_do_list) == 0:
        return
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(to_do_list):
        to_do_list[task_index]['Status'] = "completed"
        print(f"Task '{to_do_list[task_index]['task']}' marked as completed!\n")
    else:
        print("Invalid task number. Please try again.\n")

#To display menu
def display_menu():
    while True:
        print("*** To-Do List Menu ***")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

display_menu()