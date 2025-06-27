class Empolyee:
  def __init__(self):
    print("this is empolyee class")
  a=1
class progurammer(Empolyee):
   def __init__(self):
    print("this is programer class")
   b=2

class coder(progurammer):
   def __init__(self):
    super().__init__()
    print("this is coder class")
   c=3


#o=Empolyee()
#print(o.a)
#o=progurammer()
#print(o.a,o.b)
o=coder()
print(o.a,o.b,o.c)  