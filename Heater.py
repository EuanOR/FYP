from Rad import Rad

class Heater(object):

    def __init__(self, heat, power_con):
        
        self._rads = []
        self._heat = heat
        self._power_con = power_con

    def addRad(self, new_rad):
        
        self._rads.append(new_rad)

    def setHeat(self, new_heat):
        
        self._heat = new_heat

    def getHeat(self):
        
        return self._heat

    def setPowerCon(self, new_power_con):
        
        self._power_con = new_power_con

    def getPowerCon(self):
        
        return self._power_con

    def powerOn(self):
        
        for r in self._rads:

            r.activate()

    def powerOff(self):
        
        for r in self._rads:

            r.deactivate()

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

    H.powerOn()
    print("\n")
    H.powerOff()

if __name__ == "__main__":
   
    test()
