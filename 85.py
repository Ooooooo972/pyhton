class cal:
  
  def __init__(self,n):
    self.n=n
  
  def square(self):
    print(f"the square is {self.n*self.n}")
  def quqbe(self):
    print(f"the quabe is {self.n*self.n*self.n}")
  def squaroot(self):
    print(f"the squaroot is {self.n**1/2}")


  @staticmethod
  def Hello():
   print("hello there")


a=cal(45)
a.Hello()
a.square()
a.quqbe()
a.squaroot()

