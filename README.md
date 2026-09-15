# Task Manager CLI

A simple, persistent command-line to-do list application built in Python.

## Features
- Add tasks with a title and priority level (High / Medium / Low)
- View all tasks, automatically sorted by priority
- Mark tasks as complete
- Delete tasks
- Data is saved locally in `tasks.json`, so tasks persist between runs

## Tech Used
- Python 3 (standard library only — no external dependencies)
- JSON for local data persistence

## How to Run
```bash
python task_manager.py
```

Follow the on-screen menu to add, view, complete, or delete tasks.

## Example
```
==== TASK MANAGER ====
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Delete Task
5. Exit

Choose an option: 1
Enter task title: Finish resume
Priority (High/Medium/Low) [Medium]: High
Task "Finish resume" added.
```

## What This Project Demonstrates
- File I/O and data persistence (JSON read/write)
- CRUD operations (Create, Read, Update, Delete)
- Working with Python data structures (lists of dictionaries)
- Basic sorting logic (custom sort by priority)
- Clean, modular function design
