a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

def hcf(a,b):
    while b:
        a, b = b, a % b 
    return a
print("The HCF of", a, "and", b, "is", hcf(a, b))