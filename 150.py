n = int(input("How many elements? "))
lst = []

for i in range(n):
    val = input(f"Enter element {i+1}: ")
    lst.append(val)

print("List:", lst)
