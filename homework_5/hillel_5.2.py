import pickle


with open('test/data/data.pickle', 'rb') as f:
    data_new = pickle.load(f)
    for i in data_new:
        if i[-1] == 1:
            print(f"{i[0]} + {i[1]} = {i[0] + i[1]}")
        elif i[-1] == 2:
            print(f"{i[0]} - {i[1]} = {i[0] - i[1]}")
        elif i[-1] == 3:
            print(f"{i[0]} * {i[1]} = {i[0] * i[1]}")
        else:
            print(f"This is not a number.")




