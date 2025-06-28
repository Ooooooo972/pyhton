a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if (b==0):
  raise ZeroDivisionError("hey our program does not support division by zero")
else:
  print(f"The result of {a} divided by {b} is {a/b}")