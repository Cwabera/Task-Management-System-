# main.py

from task_utils import create_task, calculate_progress

tasks = []


def add_task():
    title = input()
    description = input()
    due_date = input()

    tasks.append(create_task(title, description, due_date))
    print("Task added successfully!")


def complete_task():
    try:
        index = int(input()) - 1

        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return

        tasks[index]["completed"] = True
        print("Task marked as complete!")

    except ValueError:
        print("Invalid input.")


def view_pending():
    for task in tasks:
        if not task["completed"]:
            print(task["title"])


def progress():
    print(calculate_progress(tasks))


def menu():
    while True:
        choice = input()

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