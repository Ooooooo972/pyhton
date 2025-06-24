import random

computer=random.choice([-1,0,1])
yourst=(input("enter your chose: "))
yourdic={ "s":1,"w":-1,"g":0}
reversdic={1:"snake",0:"gun",-1:"water"}
you=yourdic[yourst]
 
print(f"your chose:- {reversdic[you]}\n computer chose:- {reversdic[computer]}")
if (computer==you):
  print("it is a drow")
else:
  if(computer==-1 and you==1):
    print("you win")
  elif(computer==1 and you==0):
    print("you win") 
  elif(computer==0 and you==1):
    print("you lose") 
  elif(computer==-1 and you==0):
    print("you win") 
  elif(computer==0 and you==-1):
    print("you lose") 
  elif(computer==1 and you==-1):
    print("you lose!!")
  else:
    print("something is wrong")         