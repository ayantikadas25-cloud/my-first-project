tasks = []

while True:
    print("\n--- Student Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, 1):
                status = "Completed" if item["done"] else "Pending"
                print(i, item["task"], "-", status)

    elif choice == "3":
        number = int(input("Enter task number: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print("Task completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        number = int(input("Enter task number: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")