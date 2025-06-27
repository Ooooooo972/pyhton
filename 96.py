class complex:
  def __init__(self,r,i):
    self.r=r
    self.i=i


  def __sum__(self,c2):
    return complex(self.r+c2.r,self.i+c2.i)
  
  def _multi__(self,c2):
    real_part=self.r*c2.r-self.i*c2.i
    img_part=self.r*c2.i+self.i*c2.r
    return complex(real_part,img_part)
  
  def __str__(self):
    return f"{self.r}+{self.i}i"
    


c1=complex(1,2)
c3=complex(3,4)
print(c1 + c3)
print(c1*c3)