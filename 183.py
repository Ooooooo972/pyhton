def fun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Argument *argv :", arg)

fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
fun('Hello', 'Welcome', 'to', 'GeeksforGeeks', 'with', 'extra', 'arguments')