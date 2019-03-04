from Light import Light
import Firebase


class LightController(object):

    def __init__(self, lights):

        self._lights = lights
        self._active = Firebase.get_lights_active()

        if self._active:
            self.power_on()

    def power_on(self):

        self._active = True
        Firebase.set_lights_active(self._active)
        for l in self._lights:

            l.turn_on()

    def power_off(self):

        self._active = False
        Firebase.set_lights_active(self._active)
        for l in self._lights:

            l.turn_off()