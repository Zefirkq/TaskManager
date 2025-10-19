import re
import json
from pathlib import Path
from TaskClass import Task
from json_manager import addfile

addfile() # create 'tasks.json' if not exists

with open('tasks.json', 'r') as file:
        dict = json.load(file)
        if not len(dict["tasks"]) == 0:
            Task.id = dict["tasks"][-1]['id'] + 1       

while True:
    user_input = input('print:')
    if re.compile(r'^\s*add \"[^\"]+\"\s*$').fullmatch(user_input): # user_input format - ' add "name" '
        title = re.search(r'\"[^\"]+\"', user_input).group()
        Task.add_task(title=title)
        print(f'title: {title}')
        print('added')
        
    elif re.compile(r'^\s*update [0-9]+ \"[^\"]+\"\s*$').fullmatch(user_input):  # user_input format - ' update id "new name" '
        new_title = re.search(r'\"[^\"]+\"', user_input).group()
        id = int(user_input.split()[1]) 
        print(f'new title: {new_title}')
        print(f'new id: {id}')
        print('updated')

    elif re.compile(r'^\s*delete [0-9]+$').fullmatch(user_input):   # user_input format - ' delete id '
        id = int(user_input.split()[1]) 
        Task.delete_task(id=id)

    elif re.compile(r'^\s*mark-in-progress [0-9]+$').fullmatch(user_input):     # user_input format - ' mark-in-progress  id '
        id = int(user_input.split()[1]) 
        Task.task_status('mark-in-progress', id=id) 

    elif re.compile(r'^\s*mark-done [0-9]+$').fullmatch(user_input):    # user_input format - ' mark-done  id '
        id = int(user_input.split()[1]) 
        Task.task_status('mark-done', id=id)    

    else:
        print('wrong input')


    decide = input('want to exit?(y/n): ')
    if decide == 'y':
        break
    