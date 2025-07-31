from collections import Counter

# Creating a Counter from a list
ctr1 = Counter([1, 2, 2, 3, 3, 3])

# Creating a Counter from a dictionary
ctr2 = Counter({1: 2, 2: 3, 3: 1})

# Creating a Counter from a string
ctr3 = Counter('hello')

print(ctr1)
print(ctr2)
print(ctr3)