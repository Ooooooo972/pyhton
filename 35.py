a=int(input("Enter 1 marks: "))
b=int(input("Enter 2 marks: "))
c=int(input("Enter 3 marks: "))
total=(100*(a+b+c))/300
if(total>=40 and a>=33 and b>=33 and c>=33):
    print("you are pass",total)
else:
    print("you are fail",total)