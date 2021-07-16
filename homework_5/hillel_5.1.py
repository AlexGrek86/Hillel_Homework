import os
import pickle
import random

os.chdir('.')
os.makedirs('test/data')

with open('test/data/data.pickle', 'wb') as f:
    tuples_list = [(random.randint(1, 100),
                    random.randint(1, 100),
                    random.randint(1, 3))
                   for i in range(100)]
    pickle.dump(tuples_list, f)
