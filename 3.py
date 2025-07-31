from collections import Counter

ctr = Counter([1, 2, 2, 3, 3, 3])
common = ctr.most_common(2)

print(common)

from collections import Counter

ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])

# Addition
print(ctr1 + ctr2)  
# Subtraction
print(ctr1 - ctr2)  

# Intersection
print(ctr1 & ctr2)  
# Union
print(ctr1 | ctr2)