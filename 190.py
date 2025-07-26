import functools

# importing operator for operator functions
import operator

# initializing list
a = [1, 3, 5, 6, 2]

# using reduce with add to compute sum of list
print(functools.reduce(operator.add, a))

# using reduce with mul to compute product
print(functools.reduce(operator.mul, a))

# using reduce with add to concatenate string
print(functools.reduce(operator.add, ["geeks ", "for ", "geeks"]))