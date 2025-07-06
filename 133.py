import random
number_to_gass=random.randint(1,100)
while True:
 try:
    i=int(input("enter the number 1 to 100:"))
    if (i<number_to_gass):
      print("too tow")
    elif (i>number_to_gass):
     print("too high")

    elif(i==number_to_gass):
      print(" wow! you gass the number")
      break
 except ValueError:
  print("print enter the valid number:")