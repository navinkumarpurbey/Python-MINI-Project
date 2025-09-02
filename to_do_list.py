todo_list = []

def show_menu():
    print("\n📌 Simple To-Do List")
    print("1. Add Task ➕")
    print("2. View Tasks 👀")
    print("3. Remove Task ❌")
    print("4. Exit 🚪")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f"✅ Task added: {task}")

    elif choice == "2":
        if not todo_list:
            print("📭 No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not todo_list:
            print("📭 No tasks to remove!")
        else:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"❌ Task removed: {removed}")
            else:
                print("⚠ Invalid task number!")

    elif choice == "4":
        print("Existing... Have a productive day")
        break

    else:
        print("Invalid Choice! Please Try Again.")