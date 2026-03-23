# Task Manager Application

## Author

Charles Ngatia

---

## Description

This is a simple **Task Management System** built in Python that allows users to manage their daily tasks and track their progress.

The program uses a **list of dictionaries** to store tasks, where each task contains:

* A title
* A completion status (True/False)

---

## Features

* Add new tasks
* View all tasks
* Mark tasks as complete
* View pending tasks
* Track progress (percentage completed)
* Interactive menu system

---

## Project Structure

task_manager/
│── task_manager.py
│── README.md

---

##  How to Run the Program

### 1. Open your terminal

### 2. Navigate to the project folder

```bash
cd task_manager
```

### 3. Run the program

```bash
python3 task_manager.py
```

---

## Example Usage

```text
==== Task Manager ====
1. Add Task
2. View Tasks
3. Complete Task
4. View Pending Tasks
5. Track Progress
6. Exit
```

### Example Output

```text
Task added successfully!
1. Study Python [✗]

Task marked as complete!
Progress: 1/1 tasks completed (100.00%)
```

---

## Technologies Used

* Python 3

---

# Concepts Applied

* Lists and Dictionaries
* Functions and Modular Code
* Input Validation
* Loops and Conditionals

---

# Future Improvements

* Save tasks to a file (persistent storage)
* Add due dates
* Add task priorities
* GUI version (Tkinter or React frontend)

---

# Notes

* Input validation is included for user-friendly interaction
* Tasks are stored in memory (they reset when the program stops)

---

# Submission

GitHub Repository Link:
https://github.com/Cwabera/Task-Management-System-
