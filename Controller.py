
class Controller(object):
    
    def __init__(self, house, monitor):
        
        self._house = house
        self._monitor = monitor
    
    def getHouse(self):
        
        return self._house
    
    def setHouse(self,newHouse):
        
        self._house = newHouse
    
    def getMonitor(self):
        
        return self._monitor
    
    def setMonitor(self, newMonitor):

        self._monitor = newMonitor