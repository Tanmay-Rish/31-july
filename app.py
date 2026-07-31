tasks = []

while True:
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks found")

    elif choice == "2":
        break

    else:
        print("Invalid choice")