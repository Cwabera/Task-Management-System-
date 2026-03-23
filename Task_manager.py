# task_manager.py

from task_utils import *

tasks = []


def add_task():
    title = input("Enter task title: ")
    
    if not validate_title(title):
        print("Invalid title.")
        return
    
    tasks.append(create_task(title))
    print("Task added!")


def view_tasks():
    if not tasks:
        print("No tasks.")
        return
    
    for i, task in enumerate(tasks, 1):
        print(format_task(task, i))


def complete_task():
    view_tasks()
    
    try:
        index = int(input("Enter task number: ")) - 1
        
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task completed!")
        else:
            print("Invalid number.")
    
    except ValueError:
        print("Enter a valid number.")


def view_pending():
    pending = get_pending_tasks(tasks)
    
    if not pending:
        print("No pending tasks.")
        return
    
    for i, task in enumerate(pending, 1):
        print(format_task(task, i))


def progress():
    completed, total, percent = calculate_progress(tasks)
    print(f"{completed}/{total} completed ({percent:.2f}%)")


def menu():
    while True:
        print("\n1.Add 2.View 3.Complete 4.Pending 5.Progress 6.Exit")
        choice = input("Choose: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            view_pending()
        elif choice == "5":
            progress()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()