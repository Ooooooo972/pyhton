try:
   a=int(input("Enter a number: "))
   b=int(input("Enter another number: "))
   print(a/b)
except ZeroDivisionError as v:
   print("infinity")