#The task of an interface is to put that method and that can be used in the classes 
#the interface segregation principle states that no client should be forced to depend on methods it doesn't use
#Employee Interface
#    |          |
# Programmer    Manager 

#we break the interfaces into pieces and this prevents the subclasses from getting polluted
class Phone:
    def call(self,number):
        raise NotImplementedError()
    
    def swipe_to_unlock(self):
        raise NotImplementedError()
    
class Iphone(Phone):
    def call(self,number):
        print(f"calling from {self.number}")
        
    def swipe_to_unlock(self):
        print("IPhone unlocked")
    
#now similarly creating a Nokia phone that doesn't support touch screen or rather in other words swiping but still it has to implement the swipe_to_unlock thus it is violating the interface segregation principle
class Nokia(Phone):
    def call(self,number):
        print(f"calling from {self.number}")
        
    def swipe_to_unlock(self):
        raise NotImplementedError()
    
#here the interface segregation Principal is getting violated
        

    
    
