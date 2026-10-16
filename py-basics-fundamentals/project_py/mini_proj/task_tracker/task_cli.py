import sys
import os
import json
from datetime import datetime
from enum import Enum


if len(sys.argv) < 2:
    sys.exit("Usage: python script.py <command> <task_input>") 

command = sys.argv[1] 
t_command = command.lower()

if t_command not in ["add", "list", "update", "delete", "mark-done", "mark-in-progress", "mark-todo"]:
    sys.exit(f"Error: '{t_command}' is not a valid command. Please choose from: add, list, update, delete, mark-done, mark-in-progress, mark-todo")

FILENAME = "task_file.json"

if t_command == "add":
    if len(sys.argv) < 3:
        sys.exit("Error: Please provide a task description. Example: add 'My task'")
        
    task_info = sys.argv[2]
    
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = [] 
    else:
        tasks = []

    next_id = max((task["id"] for task in tasks), default=0) + 1

    new_task = {
        "id": next_id,
        "description": task_info,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    
    tasks.append(new_task)
   
    
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Task added successfully (ID: {new_task['id']})")

elif t_command == "list":
    if not os.path.exists(FILENAME):
        sys.exit("File does not exist yet. Add a task first!")
    
    with open(FILENAME, "r") as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []

    if not tasks:
        print("tasks not found")
        sys.exit()

    
    if len(sys.argv) > 2 :
        filter_status = sys.argv[2].lower()

        class TaskStatus(Enum):
            TODO = "todo"
            IN_PROGRESS = "in-progress"
            DONE = "done"
            
        try:
            TaskStatus(filter_status)
        except ValueError:
            print(f"Error: '{filter_status}' is not a valid task status.")
            sys.exit("Please choose from: todo, in-progress, done")

        if filter_status:
            found_status = False
            for task in tasks:
                if task["status"] == filter_status:
                    print(f"[{task['status'].upper()}] \nID: {task['id']} \nTasks: {task['description']} \nCreatedAt: {task['createdAt']} \nUpdatedAt: {task['updatedAt']}")
                    found_status = True

            if not found_status:
             print(f"No tasks found with status '{filter_status}'.")
             sys.exit()

    else:
        for task in tasks:
            print(f"[{task['status'].upper()}] \nID: {task['id']} \nTasks: {task['description']} \nCreatedAt: {task['createdAt']} \nUpdatedAt: {task['updatedAt']}")

elif t_command == "update":
    if len(sys.argv) < 4:
        sys.exit("Error: Please provide a task ID and new description. Example: update 1 'Updated task description'")

    try:
        task_id = int(sys.argv[2])
    except ValueError:
        sys.exit("Error: Task ID must be an integer.")

    new_description = sys.argv[3].lower()

    with open(FILENAME, "r") as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []

    for task in tasks:
        found_description = False
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            found_description = True
            break

    if not found_description:
        sys.exit(f"Error: Task with ID {task_id} not found.")

    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Task with ID {task_id} updated successfully.")

elif t_command == "delete":
    if len(sys.argv) < 3:
        sys.exit("Error: Please provide a task ID to delete. Example: delete 1")

    try:
        task_id = int(sys.argv[2])
    except ValueError:
        sys.exit("Error: Task ID must be an integer.")

    with open(FILENAME, "r") as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []

    for task in tasks:
        found_delete = False
        if task["id"] == task_id:
            tasks.remove(task)
            found_delete = True
            break

    if not found_delete:
        sys.exit(f"Error: Task with ID {task_id} not found.")

    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Task with ID {task_id} deleted successfully.")

elif t_command in ("mark-done", "mark-in-progress", "mark-todo"):
    command, status = t_command.split("-",1)
    if len(sys.argv) < 3:
        sys.exit("Error: Please provide a task ID and new status. Example: status 1 'in-progress'")

    try:
        task_id = int(sys.argv[2])
    except ValueError:
        sys.exit("Error: Task ID must be an integer.")


    with open(FILENAME, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []

    for task in tasks:
        found_status = False
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            found_status = True
            break

    if not found_status:
        print(f"Error: Task with ID {task_id} not found.")

    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Task {task_id} marked as {status}.")
    
