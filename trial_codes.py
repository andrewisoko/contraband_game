import json


empty_list = []

input1 = input("Abeg put sommm: ")
input2 = input("Abeg put sommm: ")

with open ("json_user_data","r") as file:
        read_data_for_signin = json.load(file)


for dictionaries in read_data_for_signin:
    
    for values in dictionaries.values():
        empty_list.append(values)
        
# for i,list_values in enumerate(empty_list):
    
    
# if input1 in empty_list and input2 in empty_list:
#     print("ok")
# else:
#     print("nono")

