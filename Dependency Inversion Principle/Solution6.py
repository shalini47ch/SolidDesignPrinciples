from abc import ABC, abstractmethod

# Abstraction
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# High-level module
class LightSwitch:
    def __init__(self, bulb: Switchable):
        self.bulb = bulb

    def turn_on(self):
        self.bulb.turn_on()

    def turn_off(self):
        self.bulb.turn_off()

# Low-level module
class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb is turned on")

    def turn_off(self):
        print("LightBulb is turned off")

# Usage
bulb = LightBulb()
switch = LightSwitch(bulb)
switch.turn_on()
switch.turn_off()
