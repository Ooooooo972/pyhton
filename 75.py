word="donkey"
with open("file.txt","r")as f:
  contant=f.read()


contant=contant.replace(word,"#####")

with open("file.txt","w")as f:
  f.write(contant)  