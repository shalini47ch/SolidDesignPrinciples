#here we will split the class into multiple functionalities and create them as instances and the specific phones can use them accordingly
class PhoneCall:
    def call(self,number):
        raise NotImplementedError()
    
class Touch:
    def swipe_to_unlock(self):
        raise NotImplementedError()
    
#now according to the functionalities they need the phones can use them
class Iphone(PhoneCall,Touch):
    def call(self,number):
          print(f"Calling {number} from iPhone")
        
    def swipe_to_unlock(self):
        print("Iphone unlocked")
        
class Nokia(PhoneCall):
    def call(self,number):
        print(f"calling {number} from Nokia")
        
obj1 = Iphone()
obj2 = Nokia()
obj1.call(91234567789)
obj1.swipe_to_unlock()
obj2.call(9876543210)

#this helps to solve the previous problem and this code obeys the interface segregation principles