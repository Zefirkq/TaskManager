import json
from datetime import datetime
with open('test.json', 'r') as file:
        dict = json.load(file)

print(dict)
print(dict["tasks"][-1]['id'])  
print(type(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
new_dict = []
