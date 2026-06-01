import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        print("Error reading file. Starting with empty task list.")
        return []


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except:
        print("Error saving tasks.")


def add_task(tasks):
    title = input("Enter task title: ").strip()

    if title == "":
        print("Task title cannot be empty.")
        return

    due_date = input("Enter due date (DD-MM-YYYY) or leave blank: ").strip()
    tag = input("Enter tag/category or leave blank: ").strip()

    task = {
        "title": title,
        "done": False,
        "due_date": due_date if due_date else "No due date",
        "tag": tag if tag else "General",
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("\nYour To-Do List:")
    print("-" * 60)

    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"

        print(f"{i}. {task['title']}")
        print(f"   Status   : {status}")
        print(f"   Due Date : {task['due_date']}")
        print(f"   Tag      : {task['tag']}")
        print(f"   Created  : {task['created_at']}")
        print("-" * 60)


def mark_done(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_no = int(input("Enter task number to mark as done: "))

        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
            return

        tasks[task_no - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_no = int(input("Enter task number to delete: "))

        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['title']}")

    except ValueError:
        print("Please enter a valid number.")


def search_by_tag(tasks):
    tag = input("Enter tag to search: ").strip().lower()

    found = False

    for i, task in enumerate(tasks, start=1):
        if task["tag"].lower() == tag:
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['title']} | {status} | Due: {task['due_date']}")
            found = True

    if not found:
        print("No tasks found with this tag.")


def menu():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST MANAGER ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Search Tasks by Tag")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_by_tag(tasks)
        elif choice == "6":
            print("Thank you for using To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


menu()