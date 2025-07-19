import math
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

print("The LCM of", a, "and", b, "is", lcm(a, b))
