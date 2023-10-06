#It allows us to depend on interfaces than on concrete classes
#violation are object instantiation in lower level modules and import statements 
# High-level module
class LightSwitch:
    def __init__(self):
        self.bulb = LightBulb()  # Violation: High-level module depends on a low-level module directly

    def turn_on(self):
        self.bulb.turn_on()

    def turn_off(self):
        self.bulb.turn_off()

# Low-level module
class LightBulb:
    def turn_on(self):
        print("LightBulb is turned on")

    def turn_off(self):
        print("LightBulb is turned off")

# Usage
switch = LightSwitch()
switch.turn_on()
switch.turn_off()
