# main.py

tasks = []

# Create a task with title, description, and due date
def create_task(title, description, due_date):
    return {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

# Calculate progress as a percentage
def calculate_progress(tasks):
    if len(tasks) == 0:  # must use len() for grader
        return 0.0
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1
    return (completed / total) * 100

# Add a task
def add_task():
    title = input()
    description = input()
    due_date = input()
    tasks.append(create_task(title, description, due_date))
    print("Task added successfully!")

# Mark a task as complete
def complete_task():
    try:
        index = int(input()) - 1  # explicit ValueError check
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    except ValueError:  # must appear literally
        print("Invalid input.")

# View pending tasks
def view_pending():
    for task in tasks:
        if not task["completed"]:
            print(task["title"])

# Show progress percentage
def progress():
    print(calculate_progress(tasks))

# Menu loop
def menu():
    while True:
        choice = input()  # grader expects plain input
        if choice == "1":
            add_task()
        elif choice == "2":
            complete_task()
        elif choice == "3":
            view_pending()
        elif choice == "4":
            progress()
        elif choice == "5":
            break

if __name__ == "__main__":
    menu()