from WeatherAPI import WeatherAPI
from Heater import Heater
from Rad import Rad

class Controller(object):

    def __init__(self,low,high, heater):
        
        self._low = low
        self._high = high
        self._heatingActive = False
        self._heater = heater

    def control(self):
    
        curTemp = WeatherAPI().getTemperature()

        if (curTemp <= self._low and not self._heatingActive):
            print(curTemp)
            self.activateHeating()
        
    
    def activateHeating(self):
        
        self._heater.powerOn()
    
    def deactivateHeating(self):
        
        self._heater.powerOff()

def test():

    H = Heater(15, 90)

    r1 = Rad(H.getHeat())
    r2 = Rad(H.getHeat())
    r3 = Rad(H.getHeat())
    r4 = Rad(H.getHeat())
    r5 = Rad(H.getHeat())
    r6 = Rad(H.getHeat())

    H.addRad(r1)
    H.addRad(r2)
    H.addRad(r3)
    H.addRad(r4)
    H.addRad(r5)
    H.addRad(r6)

    c = Controller(10,20,H)
    c.control()

if __name__ == "__main__":
    test()