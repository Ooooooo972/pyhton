import random
while True:
 choices=('r','p','s')
 your =input("rock ,papper, scissors r/p/s :-").lower()
 if (your  not  in choices):
  print("invlid choice")

 computer=random.choice(choices)
 print(f"your choice ,{your}")
 print(f"computer choice,{computer}")

 if (your==computer):
  print("tie:")
 elif(your=='r' and computer=='s'):
  print("you win")
 elif(your=='s'and computer=='p'):
  print("you win")
 elif(your=='p' and computer=='r'):
  print("you win")
 else:
  print("you loss")

 count=input("continue?(y/n):-")
 if(count=='n'):
  break