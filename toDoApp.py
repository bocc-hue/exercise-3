# toDoApp.py

tasks = []

def addtask(task):
    if not task.strip():
        print("Task cannot be empty!")
    elif task in tasks:
        print("Task already exists!")
    else:
        tasks.append(task)
        print(f"Task '{task}' added!")

def showTasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("\nYour Tasks:")
        print("-" * 20)
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        print("-" * 20)

def removetask(tasknumber):
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Invalid task number!")
    else:
        removed_task = tasks.pop(tasknumber - 1)
        print(f"Task '{removed_task}' removed!")

def main():
    while True:
        print("\nTask Manager")
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
            print("Goodbye!")
            break
        else:
            print("Wrong choice!")
main()
