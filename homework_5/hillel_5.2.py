import pickle


# with open('test/data/data.pickle', 'rb') as f:
#     data_new = pickle.load(f)
#     for i in data_new:
#         if i[-1] == 1:
#             print(f"{i[0]} + {i[1]} = {i[0] + i[1]}")
#         elif i[-1] == 2:
#             print(f"{i[0]} - {i[1]} = {i[0] - i[1]}")
#         elif i[-1] == 3:
#             print(f"{i[0]} * {i[1]} = {i[0] * i[1]}")
#         else:
#             print(f"This is not a number.")

# Perfect but I suggest to look on unpacking operation for sequences:
# Take a look how it could be solved cleaner
with open('test/data/data.pickle', 'rb') as f:
    operations = pickle.load(f)
    for operation in operations:
        l_operand, r_operand, operator = operation
        if operator == 1:
            # print(f"{l_operand} + {r_operand} = {l_operand + r_operand}")
            print(f"{l_operand + r_operand = }")
        elif operator == 2:
            # print(f"{l_operand} - {r_operand} = {l_operand - r_operand}")
            print(f"{l_operand - r_operand = }")
        elif operator == 3:
            # print(f"{l_operand} * {r_operand} = {l_operand * r_operand}")
            print(f"{l_operand * r_operand = }")
        else:
            print(f"This is not a number.")
