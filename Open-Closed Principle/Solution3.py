#to overcome the problem of mutiple switches we are using for the employees we can use polymorphism
class Employee:
    def __init__(self,name):
        self.name=name 
    
    def get_info(self):
        return f"{self.name} is an employee"
    
#similarly create a class called as Manager
class Manager(Employee):
    def __init__(self,name,department):
        super().__init__(name)
        self.department=department 
        
    def get_info(self):
        return f"{self.name} is a manager and he belongs to the {self.department}"
    
#extending is easy as we can provide different implementations with the same name 
class Programmer(Employee):
    def __init__(self,name,language):
        super().__init__(name)
        self.language=language 
        
    def get_info(self):
        return f"{self.name} knows {self.language}"
    
    
    
def print_employee(e):
    print(e.get_info())
    
emp=Employee("rty")
man=Manager("yui","IT")
prog=Programmer("tina","C++")
print_employee(emp)
print_employee(man)
print_employee(prog)

#this solves the problem of open close principle it is following the open close and we dont need to use switch cases


        
        
    