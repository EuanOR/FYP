class Room(object):

    def __init__(self, name, length, width, height, insulation, window):
        #Measurements are done in Feet.
        self._name = name
        self._length = length
        self._width = width
        self._height = height

        self._sqrFt = self._calculateSqrFt(self._length, self._width)
        self._area = self._calculateArea(self._length, self._width, self._height)

        if isinstance(insulation, bool):
            self._insulation = insulation
        else:
            self._insulation = False
        
        self._window = window

        self._doorOpen = False
    
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
    
    def _calculateArea(self,l,w,h):
        
        area = (l*w*h)
        return area
    
    def recalculateArea(self):
        
       self._area = self._calculateArea(self._length,self._width,self._height)

    def openDoor(self):
        
        self._doorOpen = True
    
    def closeDoor(self):

        self._doorOpen = False
    

def test():
    r = Room("Living room",12,15,10,True,"glazed")
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
    

if __name__ == "__main__":

    test()