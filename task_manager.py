import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    title = input("Enter task title: ").strip()
    priority = input("Priority (High/Medium/Low) [Medium]: ").strip().title() or "Medium"
    if priority not in PRIORITY_ORDER:
        priority = "Medium"
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{title}" added.\n')


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.\n")
        return
    sorted_tasks = sorted(tasks, key=lambda t: PRIORITY_ORDER.get(t["priority"], 1))
    print("\n{:<4}{:<30}{:<10}{:<8}{}".format("ID", "Title", "Priority", "Done", "Created"))
    print("-" * 65)
    for t in sorted_tasks:
        status = "Yes" if t["done"] else "No"
        print("{:<4}{:<30}{:<10}{:<8}{}".format(
            t["id"], t["title"][:28], t["priority"], status, t["created_at"]
        ))
    print()


def complete_task(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to mark complete: "))
    except ValueError:
        print("Invalid ID.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f'Task "{t["title"]}" marked complete.\n')
            return
    print("Task not found.\n")


def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print(f'Task "{t["title"]}" deleted.\n')
            return
    print("Task not found.\n")


def main():
    tasks = load_tasks()
    menu = """
==== TASK MANAGER ====
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Delete Task
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
