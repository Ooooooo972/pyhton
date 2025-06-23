r=int(input("Enter a number: "))
for i in range (2, r):
 if(r%i==0):
     print(f"{r} is not a prime number")
     break
else:
 print(f"{r} is a prime number")