a=98


def fun():
    global a
    a = 100
    print("a in fun:", a)



fun()
print("a in main:", a)