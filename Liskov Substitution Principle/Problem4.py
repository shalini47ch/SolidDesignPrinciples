#subclasses should not change the behavior of superclasses in unexpected ways 
#superclass means the parent class and subclasses means the child class
#cases where this liskov substitution principle is violated 
#Selecting on type,breaking the is a relationship,raise error in the overridden methods ,break constraints
class Employee:
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary  
    
    def get_salary(self):
            return f"the employee has a {e.salary}"
        

    
#now create an intern class and inherit from the base class called as Employee
class Intern(Employee):
    def __init__(self,name,salary):
        super().__init__(name,None)

e=Intern("abc",0)
e.get_salary()

#To solve this problem we need to remove the is a relationship that is present between employee and Intern as the data is not consistent
#Here since intern is not getting any salary but then as well it is raising issues for the other employees that is the child class it hampering the parent class
#It is important to detect it in earlier stages otherwise the only way to solve these problems is by changing the designs
        
