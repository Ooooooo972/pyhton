a = [1, 2, 3, 4]

# Using custom function in "function" parameter
# This function is simply doubles the provided number
def double(val):
  return val*3

res = list(map(double, a))
print(res)


a = [1, 2, 3, 4]

# Using lambda function in "function" parameter
# to double each number in the list
res = list(map(lambda x: x * 2, a))
print(res)