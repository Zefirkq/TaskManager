from pathlib import Path
import json


def addfile():
    if not Path('tasks.json').exists():
        tasks = {"tasks":[]}
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)

def add_to_json(dict_task):
    with open('tasks.json', 'r') as file:
        task_json = json.load(file)
        task_json["tasks"].append(dict_task)
    with open('tasks.json', 'w') as file:
        json.dump(task_json, file, indent=4)


        
