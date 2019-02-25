from WeatherAPI import WeatherAPI
from Heater import Heater
from Rad import Rad

class Monitor(object):

    def __init__(self,low,high, heater):
        
        self._low = low
        self._high = high
        self._heater = heater

        self.heatingActive = False

    def monitor(self):
    
        curTemp = WeatherAPI().getTemperature()

        if (curTemp <= self._low and not self.heatingActive):
            
            self.activateHeating()
        
    
    def activateHeating(self):
        
        self.heatingActive = True
        self._heater.powerOn()
    
    def deactivateHeating(self):
        
        self.heatingActive = False
        self._heater.powerOff()

def test():

    H = Heater(20)

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

    c = Monitor(10,20,H)
    c.monitor()

if __name__ == "__main__":
    test()