class Employee:
  company="ITC"
  name="mohan"
  def show(self):
    print(f"the name of the employ is {self.name } and the salary is {self.company}")

class coder: 
  language="pythoon"
  def printLanguage(self):
   print(f"out of all language here is your language :{self.language}")


class programmer(Employee,coder):
  company="itc infotech"
  def showlanguage(self):
    print(f"the name is {self.name} and he is good with{self.language}")


a=Employee()
b=programmer()
b.show()
b.printLanguage()
b.showlanguage()