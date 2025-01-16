class Person:
    def __init__(self,name,code):
        self.name=name
        self.code=code
class Account(Person):
    def __init__(self,name,code,pay):
        Person.__init__(self,name,code)
        self.pay=pay
class Admin(Person):
    def __init__(self,name,code,experience):
        Person.__init__(self,name,code)
        self.experience=experience 
class Employee(Person):
    def __init__(self, name, code,pay,experience):
        Account.__init__(self,name,code,pay)
        Admin.__init__(self,name,code,experience)
    def display_employee(self):
        print("---Employee Details---")
        print(f"NAME -> {self.name}") 
        print(f"CODE -> {self.code}")  
        print(f"PAY -> {self.pay}")  
        print(f"EXPERIENCE -> {self.experience}") 
name=input("name: ")
code=input("code: ")
pay=input("pay: ")
experience=input("experience: ") 
emplo=Employee(name,code,pay,experience)
emplo.display_employee()

     
                           