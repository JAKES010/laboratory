import sys
import os
import json
from datetime import datetime


if not len(sys.argv) >= 2 :
    sys.exit("cli_value : <file_name> <command> <task_input>") 
command = sys.argv[1] 
task_info = sys.argv[2]
default_data = {}
t_command = command.lower()

if t_command == "add" and len(sys.argv) == 3:
    if not os.path.exists("task_file.json") :
        with open("task_file.json", "w") as file:
            json.dump(default_data,file)
    else:
        with open("task_file.json" , "r") as file:
            json.dump()

new_task = {
    "id": 1,
    "description":task_info,
    "status":"todo",
    "createdAt":datetime.now(),
    "updatedAt":datetime.now(),
}

if t_command == "list":
    if not os.path.exists :
        os.exit("file does not exist")