class programmer:
  company="microsoft"
  def __init__(self,name,salary,pin):
    self.name=name
    self.salary=salary
    self.pin=pin


p=programmer("harry",12000,214872)
print(p.name,p.salary,p.pin,p.company)
r=programmer("carry",12000,214872)
print(r.name,r.salary,r.pin,r.company)

