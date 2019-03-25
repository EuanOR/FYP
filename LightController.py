from Light import Light
import Firebase


class LightController(object):

    def __init__(self, lights):

        self._lights = lights
        self.active = Firebase.get_lights_active()

        if self.active:
            self.power_on()

    def power_on(self):

        self.active = True
        Firebase.set_lights_active(self.active)
        for l in self._lights:

            l.turn_on()

    def power_off(self):

        self.active = False
        Firebase.set_lights_active(self.active)
        for l in self._lights:

            l.turn_off()