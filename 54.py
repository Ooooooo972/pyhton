r=int(input("Enter a number: "))

for i in range(1, r+1):
  print(" "* (r-i), end="")
  print("*"* (2*i-1), end="")
  print("")