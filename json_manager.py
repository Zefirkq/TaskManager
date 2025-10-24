import json
from TaskClass import Task
from task_tracker import filename


def addfile():
        tasks = {"tasks":[]}
        with open(filename, 'w') as file:
            json.dump(tasks, file, indent=4)   

def load_to_json():
    with open(filename, 'r') as file:
        task_json = json.load(file)
        task_json["tasks"] = Task.list_to_json()
    with open(filename, 'w') as file:
        json.dump(task_json, file, indent=4)


def load_from_json():
    with open(filename, 'r') as file:
        dict = json.load(file) 
        if not len(dict["tasks"]) == 0:
            Task.id = dict["tasks"][-1]['id'] + 1
            for task in dict["tasks"]:
                task_object = Task(id=task["id"], title=task["description"],
                                    status=task["status"], create_time=task["createdAt"], update_time=task["updatedA"])
                Task.task_list.append(task_object)
                 


        
