#Open for extension but closed for modification
#The code you are writing here is violating the open close principle
class Employee:
    def __init__(self,name):
        self.name=name 

class Manager(Employee):
    def __init__(self,name,department):
        super().__init__(name)
        self.department=department
    
def print_employee(e):
    if type(e) is Employee:
        print(f"{e.name} is an employee")
    elif type(e) is Manager:
        print(f"{e.name} is a manager of {e.department}")

em=Employee("aisha")
m=Manager("ron","IT")
print_employee(em)
print_employee(m)

#here the open close principle is getting violated as we need to check the type of each class and then call that specific function now as the code become more complicated and there are chances that the developer might forget to update some part of code.
#So having this type of if else cases violates the open close principle and it can be solved using polymorphism


            
   