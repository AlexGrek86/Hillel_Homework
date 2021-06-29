numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers_list = []
not_even_numbers_list = []
for index, value in enumerate(numbers_list):
    if index % 2 > 0 and index != 0:
        not_even_numbers_list.append((index, value))
    else:
        even_numbers_list.append((index, value))

print(even_numbers_list)
print(not_even_numbers_list)
