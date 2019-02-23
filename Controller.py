from House import House
from Room import Room
from Rad import Rad
from WeatherAPI import WeatherAPI
import time

class Controller(object):

    api = WeatherAPI()

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
    
    def calcIncrease(self, room):
        
        increase = 0.0
        if room.getRad().isActive():
            increase = room.rad.getBTU() / room.getArea()
        
        return increase
    
    def calcDecrease(self, room):
        
        decrease = 0.0 
        return decrease

    def mainLoop(self):
        
        pollTime = time.perf_counter()
        changeTime = time.perf_counter()
        
        while True:
            
            if (time.perf_counter() - pollTime) > 10.0:
                self._monitor.monitor()
                pollTime = time.perf_counter()
            
            if (time.perf_counter() - changeTime) > 30.0:
                for r in self._house.getRooms():
                    increase = self.calcIncrease(r)
                    decrease = self.calcDecrease(r)
                    change = increase - decrease
                    r.changeTemp(change)
                
                changeTime = time.perf_counter()