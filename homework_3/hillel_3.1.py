numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = []
for index, value in enumerate(numbers_list):
    if index % 2 > 0 and index != 0:
        new_list.append((index, value))
    else:
        continue

print(new_list)
