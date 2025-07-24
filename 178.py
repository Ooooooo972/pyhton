n = 5

for i in range(n):
    for j in range(n):
        if i == j:
            print("M", end=" ")
        else:
            print("0", end=" ")
    print()  # move to the next row