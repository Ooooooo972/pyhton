class Employee:
  a=1
  @classmethod
  def show(cls):
    print(f"the class attribute is {cls.a}")

e=Employee()
e.a=54


e.show()