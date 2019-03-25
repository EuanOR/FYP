from WeatherAPI import WeatherAPI

import time
import threading

NOT_INSULATED = 2
OPEN_DOOR = 0.1
OPEN_WINDOW = 0.5

FREEZING_DECREASE = 3.0
COLD_DECREASE = 2.0
MODERATE_DECREASE = 1.0



api = WeatherAPI()


class Controller(object):


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

        if room.get_door().is_open():
            decrease += OPEN_DOOR

        if room.get_window().is_open():
            if api.get_temperature() < 0:
                decrease += FREEZING_DECREASE

            elif api.get_temperature() < 10:
                decrease += COLD_DECREASE

            elif api.get_temperature() < 20:
                decrease +=  MODERATE_DECREASE
        else:
            if not self._house.is_insulated():
                if api.get_temperature() < 0:
                    decrease += (FREEZING_DECREASE/NOT_INSULATED)

                elif api.get_temperature() < 10:
                    decrease += (COLD_DECREASE/NOT_INSULATED)

                elif api.get_temperature() < 20:
                    decrease += (MODERATE_DECREASE/NOT_INSULATED)

        return decrease

    def display(self):

        print(self._house)
        print("")
        for r in self._house.get_rooms():
            print(r)
        print("\n")

    def monitor(self):
        while True:
            self._monitor.monitor()
            time.sleep(5)

    def change_temp(self):
        while True:
            for r in self._house.get_rooms():
                increase = self.calc_increase(r)
                decrease = self.calc_decrease(r)
                change = increase - decrease
                r.change_temp(change)
            self._house.calculate_average_temp()
            self.display()
            time.sleep(5)

    def run(self):

        monitor = threading.Thread(target=self.monitor)
        change = threading.Thread(target=self.change_temp)

        monitor.start()
        change.start()