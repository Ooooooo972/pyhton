rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Create empty 2D array
arr = []

print("Enter the elements row by row:")

for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Element [{i}][{j}]: "))
        row.append(val)
    arr.append(row)

print("\n2D Array:")
for row in arr:
    print(row)
