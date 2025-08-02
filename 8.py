class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

    def get_info(self):
        return f"EmployeeID:{self.id} Salary:{self.salary}"

class SalesEmployee(Employee):
    def __init__(self, id, salary, sales=0):
        super().__init__(id, salary)
        self.sales = sales

    def get_info(self):
        return f"EmployeeID:{self.id} Salary:{self.salary} Sales:{self.sales}"
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # Add real parts and imaginary parts
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
