# task_manager.py

tasks = []

# Add a new task
def add_task():
    title = input("Enter task title: ").strip()
    
    if not title:
        print("Task title cannot be empty.")
        return
    
    task = {
        "title": title,
        "completed": False
    }
    
    tasks.append(task)
    print("Task added successfully!")


# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nAll Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['title']} [{status}]")


# Mark task as complete
def complete_task():
    view_tasks()
    
    if not tasks:
        return
    
    try:
        choice = int(input("Enter task number to mark complete: "))
        
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    
    except ValueError:
        print("Please enter a valid number.")


# View pending tasks
def view_pending_tasks():
    pending = [task for task in tasks if not task["completed"]]
    
    if not pending:
        print("No pending tasks 🎉")
        return
    
    print("\nPending Tasks:")
    for i, task in enumerate(pending, start=1):
        print(f"{i}. {task['title']}")


# Track progress
def track_progress():
    if not tasks:
        print("No tasks to track.")
        return
    
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    
    progress = (completed / total) * 100
    
    print(f"Progress: {completed}/{total} tasks completed ({progress:.2f}%)")


# Menu system
def menu():
    while True:
        print("\n==== Task Manager ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. View Pending Tasks")
        print("5. Track Progress")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            view_pending_tasks()
        elif choice == "5":
            track_progress()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()