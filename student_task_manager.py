tasks = []


def add_task():
    title = input("Enter task: ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "title": title,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Task List ---")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"{i}. {task['title']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Status: {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    number = int(input("Enter task number to mark as completed: "))

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    number = int(input("Enter task number to delete: "))

    if 1 <= number <= len(tasks):
        tasks.pop(number - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")


while True:
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using Student Task Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
