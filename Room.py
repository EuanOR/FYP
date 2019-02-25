from Window import Window
from Door import Door
from Rad import Rad
#TODO Add wall thickness and door class

class Room(object):

    def __init__(self, name, length, width, height, temp, rad, door, window):
        #Measurements are done in Feet.
        self._name = name
        self._length = length
        self._width = width
        self._height = height

        self._sqrFt = self._calculateSqrFt(self._length, self._width)
        self._area = self._calculateArea(self._length, self._width, self._height)

        self._temp = temp

        if isinstance(rad, Rad):
            self._rad = rad
        
        else:
            print("Rad must be of type Rad")
        
        self._door = door
        self._window = window
    
    def __str__(self):

        outstr = "|"
        outstr += self._name
        outstr += "| "
        outstr += ("Temperature:" + str(self._temp))
        outstr += " "
        outstr += "Rad:"
        
        if self._rad.isActive():
            outstr += "On"
        else:
            outstr += "Off" 
        
        return outstr
    
    def getLength(self):

        return self._length

    def setLength(self, new_length):

        self._length = new_length
        self.recalculateSqrFt()
        self.recalculateArea()

    def getWidth(self):

        return self._width
    
    def setWidth(self, new_width):

        self._width = new_width
        self.recalculateSqrFt()
        self.recalculateArea()
    
    def getHeight(self):

        return self._height
    
    def setHeight(self, new_height):

        self._height = new_height
        self.recalculateSqrFt()
        self.recalculateArea()
    
    def getSqrFt(self):

        return self._sqrFt

    def _calculateSqrFt(self,l,w):
        
        sqrFt = (l*w)
        return sqrFt
    
    def recalculateSqrFt(self):

        self._sqrFt = self._calculateSqrFt(self._length,self._width)
    
    def getArea(self):

        return self._area
    
    def _calculateArea(self, l, w, h):
        
        area = (l*w*h)
        return area
    
    def recalculateArea(self):
        
       self._area = self._calculateArea(self._length,self._width,self._height)

    def getTemp(self):
        
        return self._temp
    
    def setTemp(self,newTemp):

        self._temp = newTemp
    
    def changeTemp(self, change):

        self._temp += change
    
    def getRad(self):

        return self._rad
    
    def setRad(self, newRad):

        if isinstance(newRad, Rad):
            self._rad = newRad

    def openDoor(self):
        
        self._door.openDoor()
    
    def closeDoor(self):

        self._door.closeDoor()

    def openWindow(self):

        self._window.openWindow()
    
    def closeWindow(self):

        self._window.closeWindow()
    

def test():

    w = Window(2)
    d = Door(2.0)
    r = Rad(3000)
    r = Room("Living room",12,15,10,10.5,r,d,w)
    print(r.getLength())
    print(r.getWidth())
    print(r.getHeight())
    print(r.getSqrFt())
    print(r.getArea())

    r.setLength(9)
    r.setWidth(15)
    r.setHeight(12)

    print(r.getLength())
    print(r.getWidth())
    print(r.getHeight())
    print(r.getSqrFt())
    print(r.getArea())

    r.changeTemp(-1)
    print(r.getTemp())

    print(r)
    

if __name__ == "__main__":

    test()