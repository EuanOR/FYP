from WeatherAPI import WeatherAPI
from Heater import Heater
from Rad import Rad

import Firebase

import time


class Monitor(object):

    def __init__(self, low, high, heater, light_controller, kitchen_controller, bedroom_controller, utility_room_controller):

        self._low = low
        self._high = high
        self._heater = heater
        self._light_controller = light_controller
        self._kitchen_controller = kitchen_controller
        self._bedroom_controller = bedroom_controller
        self._utility_room_controller = utility_room_controller

    def get_low(self):

        return self._low

    def get_high(self):

        return self._high

    def monitor(self):

        self._check_heating()

        self._check_lights()

        self._check_kitchen()

        self._check_bedroom()

        self._check_utility_room()

    def _check_heating(self):
        cur_temp = int(WeatherAPI().get_temperature())

        # If the heating isnt on perform these checks
        if not self._heater.active:
            # If the current temperature is below the threshold or the heating has been remotely activated
            if (cur_temp <= Firebase.get_heating_threshold() and Firebase.heating_automated()) \
                    or Firebase.get_heating_active():
                self._heater.power_on()

        # If the heating is on perform these checks
        if self._heater.active:
            # If the heating has been deactivated remotely
            if not Firebase.get_heating_active():
                self._heater.power_off ()

    def _check_lights(self):
        # TODO Get rid of below variables, directly use Firebase and Time
        start_time = str(Firebase.get_lights_start())
        end_time = str(Firebase.get_lights_end())
        curtime = str(time.strftime("%H:%M"))

        # If the lights arent on perform these checks
        if not self._light_controller.active:
            # If automations enabled and the current time's in between the threshold
            # Check has the lights been activated remotely
            if ((start_time <= curtime < end_time)
                    and Firebase.lights_automated()) or Firebase.get_lights_active():
                self._light_controller.power_on()

        # If the lights are on perform these checks
        elif self._light_controller.active:
            # Check the lights have been deactivated remotely
            # TODO figure out the logic
            if ((curtime < start_time) or (curtime >= end_time) and Firebase.lights_automated()) \
                    or not Firebase.get_lights_active():
                self._light_controller.power_off()

    def _check_kitchen(self):
        if not self._kitchen_controller.kettle_active:
            if Firebase.get_kettle_active():
                self._kitchen_controller.activate_kettle()

        if self._kitchen_controller.oven_active:
            if not Firebase.get_oven_active():
                self._kitchen_controller.deactivate_oven()

        elif not self._kitchen_controller.oven_active:
            if Firebase.get_oven_active():
                self._kitchen_controller.activate_oven()

        if self._kitchen_controller.toaster_active:
            if not Firebase.get_toaster_active():
                self._kitchen_controller.deactivate_toaster()

        elif not self._kitchen_controller.toaster_active:
            if Firebase.get_toaster_active():
                self._kitchen_controller.activate_toaster()

    def _check_bedroom(self):
        if self._bedroom_controller.eb_active:
            if not Firebase.get_eb_active():
                self._bedroom_controller.deactivate_eb()
        elif not self._bedroom_controller.eb_active:
            if Firebase.get_eb_active():
                self._bedroom_controller.activate_eb()

    def _check_utility_room(self):
        if self._utility_room_controller.dryer_active:
            if not Firebase.get_dryer_active():
                self._utility_room_controller.deactivate_dryer()
        elif not self._utility_room_controller.dryer_active:
            if Firebase.get_dryer_active():
                self._utility_room_controller.activate_dryer()

def test():
    H = Heater(20)

    r1 = Rad(H.get_heat())
    r2 = Rad(H.get_heat())
    r3 = Rad(H.get_heat())
    r4 = Rad(H.get_heat())
    r5 = Rad(H.get_heat())
    r6 = Rad(H.get_heat())

    H.add_rad(r1)
    H.add_rad(r2)
    H.add_rad(r3)
    H.add_rad(r4)
    H.add_rad(r5)
    H.add_rad(r6)

if __name__ == "__main__":
    test()
