import sys
import os
import json
from datetime import datetime

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

    next_id = 1
    for task in tasks :
        next_id = task["id"] 
        if task["id"] == next_id :
            next_id+=1

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
    print(f"Task added successfully (ID: {new_task["id"]})")

elif t_command == "list":
    if not os.path.exists(FILENAME):
        sys.exit("File does not exist yet. Add a task first!")
    
    if len(sys.argv) > 2 :
        filter_status = sys.argv[2].lower()
        
    with open(FILENAME, "r") as file:
        tasks = json.load(file)
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            print(f"[{task['status'].upper()}] \nID: {task['id']} \nTasks: {task['description']} \nCreatedAt: {task['createdAt']} \nUpdatedAt: {task['updatedAt']}")

elif t_command == "update":
    pass