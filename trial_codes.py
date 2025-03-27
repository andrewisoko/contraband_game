import json


new_data = {"name": "Charlie", "age": 22}

with open('json_user_data', 'r') as file:
    data = json.load(file)

data.append(new_data)

with open('json_user_data', 'w') as file:
    json.dump(data, file, indent=4)

print("Data appended successfully!")
