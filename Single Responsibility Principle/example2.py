#In this code we will move the storage code from the employee code so that the single responsibility principle holds good
class Employee:
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary 
        
    def raise_salary(self,factor):
        return self.salary*factor 
    
class EmployeeStorage:
    xml_filename="emp1.xml"
    
    def save_as_xml(self,employee):
        with open(self.xml_filename,"w") as file:
             file.write(f"<xml><name>{employee.name}</name><salary>{employee.salary}</salary></xml>")
            
e=Employee("ronita",2000)
s=EmployeeStorage()
s.save_as_xml(e)

#This code solves the problem of single responsibility principle as the business and the storage logic as written separately and each class has a single responsibility

            
    
    