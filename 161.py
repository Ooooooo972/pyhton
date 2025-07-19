a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

 
def lcm(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1
print("The LCM of", a, "and", b, "is", lcm(a, b))