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

    def get_house(self):

        return self._house

    def set_house(self, house):

        self._house = house

    def get_monitor(self):

        return self._monitor

    def set_monitor(self, monitor):

        self._monitor = monitor

    def calc_increase(self, room):

        increase = 0.0
        rad = room.get_rad()

        if rad.is_active() and (self._house.average_temp < self._monitor.get_high()):
            increase = rad.getBTU() / room.get_area()

        return increase

    def calc_decrease(self, room):

        decrease = 0.0

        if not self._house.is_insulated():
            decrease += -0.1
        if room.get_door().is_open():
            decrease += 0.1
        if room.get_window().is_open():
            decrease += 0.5

        return decrease

    def display(self):

        print(self._house)
        print(self._monitor._heater)
        for r in self._house.get_rooms():
            print(r)

    def monitor(self):
        while True:
            self._monitor.monitor()
            time.sleep(10)

    def change_temp(self):
        while True:
            for r in self._house.get_rooms():
                increase = self.calc_increase(r)
                decrease = self.calc_decrease(r)
                change = increase - decrease
                r.change_temp(change)
            self._house.calculate_average_temp()
            self.display()
            time.sleep(15)

    def run(self):

        monitor = threading.Thread(target=self.monitor)
        change = threading.Thread(target=self.change_temp)

        monitor.start()
        change.start()
