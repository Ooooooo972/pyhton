# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))


# Example: Check if a number is even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(4))  
print(check(7))