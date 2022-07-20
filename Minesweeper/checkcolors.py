import pickle
with open('colors.p', 'rb') as f:
    new_dict = pickle.load(f)

print(new_dict)
