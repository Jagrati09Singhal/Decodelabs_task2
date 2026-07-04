import os

tasks = []

# Load tasks from file
if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        for line in file:
            task_data = line.strip().split("|")
            tasks.append({
                "task": task_data[0],
                "status": task_data[1]
            })

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append({
            "task": task_name,
            "status": "Pending"
        })
        print("✅ Task Added Successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} [{task['status']}]")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} [{task['status']}]")

            try:
                num = int(input("Enter task number to complete: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["status"] = "Completed"
                    print("✅ Task Marked as Completed!")
                else:
                    print("Invalid Task Number!")
            except:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} [{task['status']}]")

            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    deleted = tasks.pop(num - 1)
                    print(f"❌ '{deleted['task']}' Deleted Successfully!")
                else:
                    print("Invalid Task Number!")
            except:
                print("Please enter a valid number.")

    elif choice == "5":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task["task"] + "|" + task["status"] + "\n")

        print("💾 Tasks Saved Successfully!")

    elif choice == "6":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task["task"] + "|" + task["status"] + "\n")

        print("Thank You For Using To-Do List!")
        break

    else:
        print("Invalid Choice! Try Again.")  