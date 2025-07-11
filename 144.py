# Two arrays (lists)
a = [1, 2, 3,45]
b = [4, 5, 6,43]

result = []

for i in range(len(a)):
    result.append(a[i] + b[i])

print("Resultant array:", result)
