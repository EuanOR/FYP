from Rad import Rad
import Firebase


class Heater(object):

    def __init__(self, rads):

        self._rads = rads
        self.active = Firebase.get_heating_active()

        if self.active:
            self.power_on()

    def __str__(self):

        outstr = "Heater:"

        if self.active:
            outstr += "On"

        else:
            outstr += "Off"

        outstr += " "
        outstr += ("Rads:" + str(len(self._rads)))

        return outstr

    def add_rad(self, rad):

        self._rads.append(rad)

    def power_on(self):

        self.active = True
        Firebase.set_heating_active(self.active)
        for r in self._rads:
            r.activate()

    def power_off(self):

        self.active = False
        Firebase.set_heating_active(self.active)
        for r in self._rads:
            r.deactivate()


def test():
    H = Heater(15)

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

    print(H)

    H.power_on()
    print("\n")
    H.power_off()


if __name__ == "__main__":
    test()
