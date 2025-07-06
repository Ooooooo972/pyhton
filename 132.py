import random
while True:
 p=input('roll the dice?(y/n):')
 if p=='y':
  d1=random.randint(1,6)
  d2=random.randint(1,6)

  print(f'({d1},{d2})')
 
 elif p=='n':
  print("thanks for palying")
  break
 else:
  print ("invalid choice")