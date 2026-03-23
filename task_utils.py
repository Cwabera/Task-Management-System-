# task_utils.py

# Create a new task
def create_task(title):
    return {
        "title": title,
        "completed": False
    }


# Validate task title
def validate_title(title):
    return bool(title.strip())


# Format a single task for display
def format_task(task, index):
    status = "✓" if task["completed"] else "✗"
    return f"{index}. {task['title']} [{status}]"


# Get pending tasks
def get_pending_tasks(tasks):
    return [task for task in tasks if not task["completed"]]


# Calculate progress
def calculate_progress(tasks):
    if not tasks:
        return 0, 0, 0  # completed, total, percentage
    
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    percentage = (completed / total) * 100
    
    return completed, total, percentage