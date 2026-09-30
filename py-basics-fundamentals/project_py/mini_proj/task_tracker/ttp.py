import sys
import json
import os

file_name = "task_file.json"
default_data = {"tasks" : []}

if len(sys.argv) < 3 :
    sys.exit("Too few arguments")

tasks = sys.argv[2]
p_command = sys.argv[1]

if not os.path.exists(file_name) or os.path.getsize(file_name) == 0 :
    with open (file_name, "w") as file :
        json.dump(default_data, file)

if p_command == "Add":
    with open(file_name, "r") as file :
       tsk_list = json.load(file)

       tsk_list["tasks"].append(tasks)
    with open(file_name, "w") as file :
        json.dump(tsk_list,file)
        print(f"ADDED : {tasks}")