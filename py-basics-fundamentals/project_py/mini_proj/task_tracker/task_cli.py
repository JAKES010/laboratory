import sys
import os
import json
from datetime import datetime
from enum import Enum


if len(sys.argv) < 2:
    sys.exit("Usage: python script.py <command> <task_input>") 

command = sys.argv[1] 
t_command = command.lower()

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
            for task in tasks:
                if task["status"] == filter_status:
                    print(f"[{task['status'].upper()}] \nID: {task['id']} \nTasks: {task['description']} \nCreatedAt: {task['createdAt']} \nUpdatedAt: {task['updatedAt']}")
        else:
            print(f"No tasks found with status '{filter_status}'.")
            sys.exit()

    else:
        for task in tasks:
            print(f"[{task['status'].upper()}] \nID: {task['id']} \nTasks: {task['description']} \nCreatedAt: {task['createdAt']} \nUpdatedAt: {task['updatedAt']}")

elif t_command == "update":
    pass