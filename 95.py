class employee:
  salary = 1000
  increment = 100
  
  @property
  def salaryafterinc(self):
    return self.salary +  self.salary*(self.increment/100)
  
  @salaryafterinc.setter
  def salaryafterinc (self, salary):
    self.increment= ((salary/self.salary)-1)*100

e=employee()
#print(e.salaryafterinc())
e.salaryafterinc= 2000
print(e.increment)