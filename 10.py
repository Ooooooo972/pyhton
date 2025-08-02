a = (1)
b = (1,)
print(type(a))
print(type(b))
def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))
def outer():
    message = "Hello"
    def inner():
        print(message)
    return inner

f = outer()
f()
def mystery(n):
    if n == 0:
        return 0
    else:
        return n + mystery(n - 1)

print(mystery(3))

x = 10
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()

print(outer())