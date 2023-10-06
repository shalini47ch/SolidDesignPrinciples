class Employee:
    xml_filename="emp.xml"
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary 
        
    def raise_salary(self,factor):
        return self.salary*factor 
    
    def save_as_xml(self):
        with open(self.xml_filename,"w") as file:
             file.write(f"<xml><name>{self.name}</name><salary>{self.salary}</salary></xml>")
            
#Here we need the xml file only the in the storage part but the developers writing the code would be confused 
            
            
e=Employee("abc",1000)
print(e.raise_salary(10))
e.save_as_xml()

#This code is violating the single responsibility principle as the storage logic is also written in the employee class but the business and the storage logic should be separate
#So we need to move this save_as xml to a new class called as employee storage 