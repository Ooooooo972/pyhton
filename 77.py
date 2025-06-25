with open("log.txt")as f:
  contant=f.readlines()
lineo=1
for line in contant:
   if("Pragmatic" in contant):
    print(f" yes  JavaScript  is present:{lineo}")
    break
   lineo+=1
else:
  print(" no JavaScript is not present")