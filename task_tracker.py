import re
from pathlib import Path
from TaskClass import Task
from json_manager import addfile, load_from_json
from sys import exit

while True:
    filename = input('print jsonfile name: ')
    if not Path(filename).exists():
        print('there is no such file')
        create_decision = input('want to create new with that name?(1 - yes, 0 - no): ')
        if create_decision == '1':
            addfile(filename) # create 'tasks.json' if not exists
            break
        elif create_decision == '0':
            loop_decision = input('exit?(1 - yes, 0 - no):')
            if loop_decision == '1':
                exit()           
        else:
            print('wrong input')
    

load_from_json()       

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
    