from datetime import datetime
import json
from json_manager import load_to_json, load_from_json

class Task:
    task_list = []
    id = 1
    def __init__(self, id, title, create_time='', update_time='-', status= 'to_do'):
        self.id = id
        self.description = title
        self.status = status
        self.createdAt = create_time
        self.updatedA = update_time

    def add_task(title):
        id = Task.id
        description = title
        create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task = Task(id=id, title=description, create_time=create_time)
        Task.task_list.append(task)
        Task.id += 1
        load_to_json()        
        

    def update_task(id, new_title):
        for task in Task.task_list:
            if id == task.id:
                task.description = new_title
                task.updatedA = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        load_to_json()        

    def delete_task(id):
        for task in Task.task_list:
            if id == task.id:
                Task.task_list.remove(task)
        load_to_json()        

    def task_status(status, id):
        for task in Task.task_list:
            if id == task.id:
                task.status = status
        load_to_json()        

    def list_to_json():
        t_list = []
        for task in Task.task_list:
            dict = {"id": task.id, "description": task.description,
                            "status": task.status, "createdAt": task.createdAt,
                              "updatedA": task.updatedA }
            t_list.append(dict)
            return t_list
      
            
    
    def all_tasks():
        pass

    def done_tasks():
        pass

    def in_progress_tasks():
        pass

    def to_do_tasks(tasks):
        pass