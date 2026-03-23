# task_utils.py

def create_task(title, description, due_date):
    return {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }


def calculate_progress(tasks):
    if not tasks:
        return 0.0

    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    
    return (completed / total) * 100  # ONLY return percentage