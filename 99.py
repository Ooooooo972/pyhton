class vector:
  def __init__(self, x):
    self.x = x
  


  def __len__(self):
    return len(self.x)
  


v1=vector({1,2,3})
print(len(v1))