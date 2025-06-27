class Employee:
  company="ITC"
  def show(self):
    print(f"the name of the employ is {self.name } and the salary is {self.salary}")



class programmer(Employee):
  company="itc infotech"
  def showlanguage(self):
    print(f"the name is {self.name} and he is good with{self.language}")


a=Employee()
b=programmer()
print(a.company,b.company)