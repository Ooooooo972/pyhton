from itertools import accumulate
from operator import add

# Cumulative sum with accumulate
a = [1, 2, 3, 4, 5]
res = accumulate(a, add)

print(list(res))