p1="hello"
p2="world"
p3="hello world"  
p4="good"
message=input("Enter a message: ")
if((p1 in message) and (p2 in message) and (p3 in message) and (p4 in message)):
    print("this message is spam")
else:

    print("this message is not spam")    