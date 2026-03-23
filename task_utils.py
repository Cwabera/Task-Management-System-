# task_utils.py

def create_task(title):
    return {"title": title, "completed": False}


def validate_title(title):
    return bool(title.strip())


def format_task(task, index):
    status = "✓" if task["completed"] else "✗"
    return f"{index}. {task['title']} [{status}]"


def get_pending_tasks(tasks):
    return [task for task in tasks if not task["completed"]]


def calculate_progress(tasks):
    if not tasks:
        return 0, 0, 0
    
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    percent = (completed / total) * 100
    
    return completed, total, percent