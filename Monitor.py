from WeatherAPI import WeatherAPI
from Heater import Heater
from Rad import Rad

import Firebase


class Monitor(object):

    def __init__(self, low, high, heater, light_controller):

        self._low = low
        self._high = high
        self._heater = heater
        self._light_controller = light_controller

        self.heating_active = Firebase.get_heating_active()
        self._lights_active = Firebase.get_lights_active()

    def get_low(self):

        return self._low

    def get_high(self):

        return self._high

    def monitor(self):

        self._check_heating()

        self._check_lights()

    def activate_heating(self):

        self.heating_active = True
        self._heater.power_on()

    def deactivate_heating(self):

        self.heating_active = False
        self._heater.power_off()

    def _check_heating(self):
        cur_temp = WeatherAPI().get_temperature()

        # If the heating isnt on perform these checks
        if not self.heating_active:
            # If the current temperature is below the threshold or the heating has been remotely activated
            if (cur_temp <= Firebase.get_heating_threshold() and Firebase.heating_automated()) \
                    or Firebase.get_heating_active():
                self.activate_heating()

        # If the heating isnt on perform these checks
        if self.heating_active:
            # If the heating has been deactivated remotely
            if not Firebase.get_heating_active():
                self.deactivate_heating()

    def activate_lights(self):

        self._lights_active = True
        self._light_controller.power_on()

    def deactivate_lights(self):

        self._lights_active = False
        self._light_controller.power_off()

    def _check_lights(self):

        # If the lights arent on perform these checks
        if not self._lights_active:
            # Check has the lights been activated remotely
            if Firebase.get_lights_active():
                self.activate_lights()

        # If the lights are on perform these checks
        if self._lights_active:
            # Check the lights have been deactivated remotely
            if not Firebase.get_lights_active():
                self.deactivate_lights()


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

    c = Monitor(10, 20, H)
    c.monitor()


if __name__ == "__main__":
    test()
