from House import House
from Room import Room
from Rad import Rad
from WeatherAPI import WeatherAPI

import time
import threading

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
        rad = room.getRad()
        
        if rad.isActive():
            increase = rad.getBTU() / room.getArea()
        
        return increase
    
    def calcDecrease(self, room):
        
        decrease = 0.0 
        if self._house.isInsulated():
            decrease += -0.1
        return decrease
    
    def display(self):

        print(self._house)
        for r in self._house.getRooms():
            print(r)
        print(self._monitor._heater)
    
    def monitor(self):
        while True:
            self._monitor.monitor()
            time.sleep(10)
    
    def changeTemp(self):
        while True:
            for r in self._house.getRooms():
                increase = self.calcIncrease(r)
                decrease = self.calcDecrease(r)
                change = increase - decrease
                r.changeTemp(change)
            self._house.calculateAverageTemp()
            self.display()
            time.sleep(30) 

    def run(self):
        
        monitor = threading.Thread(target = self.monitor)
        change = threading.Thread(target = self.changeTemp)

        monitor.start()
        change.start()