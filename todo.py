# Simple To-Do List App

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("📭 No tasks available")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n==== TO-DO LIST MENU ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print(" Task added!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f" Removed: {removed}")
            else:
                print("Invalid task number")
        except:
            print("Please enter a valid number")

    elif choice == "4":
        print("Exiting To-Do List. Bye!")
        break

    else:
        print("Invalid choice. Try again.")