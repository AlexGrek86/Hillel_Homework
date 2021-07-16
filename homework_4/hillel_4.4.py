import re


list_names = ["FirstItem", "FriendsList", "MyTuple"]
new_list = []

for i in list_names:
    changed_list = re.sub(r'(?<!^)(?=[A-Z])', '_', i).lower()
    new_list.append(changed_list)

print(new_list)
