with open("log.txt")as f:
  contant=f.read()


if("JavaScript " in contant):
  print(" yes  JavaScript  is present")
else:
  print(" no JavaScript is not present")