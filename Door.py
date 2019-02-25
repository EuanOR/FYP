class Door(object):

    def __init__(self,thickness):

        if thickness> 1.0 and thickness < 3.0:
            self._thickness = thickness
        else:
            print("Door must be between 1 and 3 inches thick")
        
        self._open =  False
    
    def getThickness(self):

        return self._thickness

    def setThickness(self, newThickness):

        if newThickness> 1.0 and newThickness < 3.0:

            self._thickness = newThickness
        
        else:

            print("Door must be between 1 and 3 inches thick")

    def openDoor(self):

        self._open = True
    
    def closeDoor(self):

        self._open =  False