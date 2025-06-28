n=int(input("Enter the no"))


table=[n*i for i in range(1,11)]
with open ("114.txt","a") as f:
  f.write(f"table of {n}: {str(table)}\n")