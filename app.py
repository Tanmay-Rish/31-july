tasks = []

while True:
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks found")

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "3":
        break

    else:
        print("Invalid choice")