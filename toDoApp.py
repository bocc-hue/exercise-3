# toDoApp.py

tasks = []

def addtask(task):
    if not task.strip():
        print("Task cannot be empty!")
    elif task in tasks:
        print("Task already exists!")
    else:
        tasks.append(task)
        print(f"Task '{task}' added!")  # Retain the improved message from the main branch

def showTasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("\nYour Tasks:")  # Retain the improved formatting from the main branch
        print("-" * 20)
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        print("-" * 20)

def removetask(tasknumber):
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Invalid task number!")
    else:
        removed_task = tasks.pop(tasknumber - 1)  # Retain the improved message from the main branch
        print(f"Task '{removed_task}' removed!")

def main():
    while True:
        print("\nTask Manager")  # Retain the improved formatting from the main branch
        print("=" * 20)
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        print("=" * 20)
        ch = input("Enter choice: ")
        if ch == "1":
            t = input("Enter task: ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            try:
                n = int(input("Enter task number to remove: "))
                removetask(n)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif ch == "4":
            print("Goodbye!")  # Retain the improved exit message from the main branch
            break
        else:
            print("Wrong choice!")
main()
