To-Do List Manager (Python CLI)

LINKEDIN POST LINK
https://www.linkedin.com/posts/esha-ghosh_github-eshag23syntecxhubto-dolistmanager-activity-7471088305435201537-Bn6G?utm_source=share&utm_medium=member_ios&rcm=ACoAAFFbqJMB3C11ce_6iHE3z-F1nQd6d4mvOkg


Project Overview

The To-Do List Manager is a command-line application developed in Python that helps users manage their daily tasks efficiently. Users can add, view, delete, mark tasks as completed, and search tasks by tags. The application stores task data in a JSON file, ensuring that tasks remain saved even after the program is closed and reopened.

Features
Add new tasks
View all tasks
Mark tasks as completed
Delete tasks
Search tasks by tag/category
Store tasks permanently using JSON files
Error handling for invalid inputs
Modular design using functions
Support for due dates and task categories
Technologies Used
Python 3
JSON File Handling
Command Line Interface (CLI)

How to Run
Step 1: Install Python

Verify Python installation:

python --version

or

py --version
Step 2: Run the Program

Navigate to the project folder and execute:

python todo.py

or

py todo.py
Menu Options
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Search Tasks by Tag
6. Exit
Example Usage
Add Task
Enter task title: Complete Python Project
Enter due date (DD-MM-YYYY): 05-06-2026
Enter tag/category: College
View Tasks
1. Complete Python Project
   Status   : Pending
   Due Date : 05-06-2026
   Tag      : College
Mark Task as Done
Enter task number to mark as done: 1
Task marked as done.
JSON Storage Example
[
    {
        "title": "Complete Python Project",
        "done": false,
        "due_date": "05-06-2026",
        "tag": "College",
        "created_at": "01-06-2026 18:20"
    }
]
Concepts Used
File Handling
Reading data from files
Writing data to files
Persistent storage
JSON Operations
json.load()
json.dump()
Functions
add_task()
view_tasks()
delete_task()
mark_done()
search_by_tag()
Exception Handling
Handling invalid inputs
Handling file-related errors
Data Structures
Lists
Dictionaries
Learning Outcomes

After completing this project, the following concepts are understood:

Python programming fundamentals
File handling operations
JSON data storage
Function-based programming
Error handling techniques
Menu-driven application development
Future Enhancements
Task priority levels
Task reminders
Task editing functionality
Graphical User Interface (GUI)
Database integration using SQLite/MySQL

Conclusion

The To-Do List Manager is a simple yet effective Python application that demonstrates file handling, JSON storage, modular programming, and error handling. It provides a practical solution for organizing and tracking daily tasks while showcasing core Python programming concepts.
