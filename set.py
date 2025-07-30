p=set()
print(p)
set1 = set("geeks of geeks")
print(set1)
# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
set1.copy()
print (set1.union({6, 5, 8}))
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

set1.discard(10)  # No error raised
print(set1)