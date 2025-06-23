p=int(input("Enter a number: ") )
for i in range (1, p+1):
    if(i==1 or i==p):
        print("*"*p, end="")
    else:
        print("*",end="")
        print(" " * ( p-2), end="")
        print("*", end="")
    
    print("")