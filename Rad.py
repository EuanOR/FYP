class Rad(object):

    def __init__(self, BTU):
        #British Thermal Units.
        #BTU is the amount of heat required to raise the temperature of 1lb of water by a degree.
        self._BTU = BTU
        self._active = False
    
    def setBTU(self, new_BTU):
        
        self._BTU = new_BTU

    def getBTU(self):
        
        return self._BTU

    def activate(self):
        
        self._active = True

    def deactivate(self):
        
        self._active = False

    def isActive(self):

        return self._active