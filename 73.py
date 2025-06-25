import random

def game( ):
  print("you are playing game...:")
  score=random.randint(1,62)
  with open("highscor.txt") as f:
    highscor=f.read()
    if(highscor!=""):
      highscor=int(highscor)
    else:
      highscor=0

  print(f"your score :{score}")
  if(score>highscor):
    with open("highscor.txt","w") as f:
      f.write(str(score))
      return score
    

game()    

    