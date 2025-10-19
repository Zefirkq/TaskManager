from datetime import datetime
import json
from json_manager import add_to_json

class Task:
    task_list = []
    id = 1
    def __init__(self, id, title, create_time='', update_time='-'):
        self.id = id
        self.description = title
        self.status = 'to-do'
        self.createdAt = create_time
        self.updatedA = update_time

    def add_task(title):
        id = Task.id
        description = title
        create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task = Task(id=id, title=description, create_time=create_time)
        Task.task_list.append(task)
        Task.id += 1
        dict = {"id": task.id, "description": task.description,
                            "status": task.status, "createdAt": task.createdAt,
                              "updatedA": task.updatedA }
        add_to_json(dict_task=dict)        
        

    def update_task(id, new_title):
        for task in Task.task_list:
            if id == task.id:
                task.description = new_title
                task.updatedA = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def delete_task(id):
        for task in Task.task_list:
            if id == task.id:
                Task.task_list.remove(task)

    def task_status(status, id):
        for task in Task.task_list:
            if id == task.id:
                task.status = status
    
    '''def dict_for_json(id):
        for task in Task.task_list:
            if id == task.id:
                dict = {"id": task.id, "description": task.description,
                            "status": task.status, "createdAt": task.create_time,
                              "updatedA": task.update_time }
        return dict'''      
            
    
    def all_tasks():
        pass

    def done_tasks():
        pass

    def in_progress_tasks():
        pass

    def to_do_tasks(tasks):
        pass