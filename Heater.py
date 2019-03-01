from Rad import Rad
from Room import Room
import Firebase
class Heater(object):

    def __init__(self, rooms):
        
        self._rads = []
        for r in rooms:
            self._rads.append(r.getRad())
        self._active = False

    
    def __str__(self):

        outstr = "Heater:"

        if self._active:
            outstr += "On"
        
        else:
            outstr += "Off"

        outstr += " "
        outstr += ("Rads:" + str(len(self._rads)))

        return outstr

    def addRad(self, newRad):
        
        self._rads.append(newRad)

    def setHeat(self, newHeat):
        
        self._heat = newHeat

    def getHeat(self):
        
        return self._heat

    def setPowerCon(self, newPowerCon):
        
        self._powerCon = newPowerCon

    def getPowerCon(self):
        
        return self._powerCon

    def powerOn(self):
        
        self._active = True
        Firebase.setHeating(self._active)
        for r in self._rads:
            r.activate()

    def powerOff(self):
        
        self._active = False
        Firebase.setHeating(self._active)
        for r in self._rads:
            r.deactivate()

def test():
    
    H = Heater(15)

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

    print(H)

    H.powerOn()
    print("\n")
    H.powerOff()

if __name__ == "__main__":
   
    test()