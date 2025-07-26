from functools import reduce

# Summing numbers with reduce and lambda
a = [1, 2, 3, 4, 5,7]
res = reduce(lambda x, y: x *y, a)

print(res)