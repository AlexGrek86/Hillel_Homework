names = ('Adam Miller', 'Bruno Smith', 'Calvin Brown',
         'Dan Wilson', 'Edgar Taylor', 'Adam Miller')
unique_names = []

for i in names:
    if i in unique_names:
        continue
    else:
        unique_names.append(i)

print(unique_names)
