from Window import Window
from Door import Door
from Rad import Rad
from Light import Light


class Room(object):
    def __init__(self, name, length, width, height, temp, rad, door, light, window):
        # Measurements are done in Feet.
        self._name = name
        self._length = length
        self._width = width
        self._height = height

        self._sqrFt = self._calculateSqrFt(self._length, self._width)
        self._area = self._calculate_area(self._length, self._width, self._height)

        self._temp = temp

        if isinstance(rad, Rad):
            self._rad = rad

        else:
            print("Rad must be of type Rad")

        self._door = door
        self._light = light
        self._window = window

    def __str__(self):

        outstr = "|"
        outstr += self._name
        outstr += "| "
        outstr += ("Temperature:" + str(round(self._temp, 2)))
        outstr += " "
        outstr += "Rad:"

        if self._rad.is_active():
            outstr += "On"
        else:
            outstr += "Off"

        outstr += " "
        outstr += "Light:"

        if self._light.is_on():
            outstr += "On"
        else:
            outstr += "Off"

        return outstr

    def get_length(self):

        return self._length

    def set_length(self, length):

        self._length = length
        self.recalculateSqrFt()
        self.recalculate_area()

    def get_width(self):

        return self._width

    def set_width(self, width):

        self._width = width
        self.recalculateSqrFt()
        self.recalculate_area()

    def get_height(self):

        return self._height

    def set_height(self, height):

        self._height = height
        self.recalculateSqrFt()
        self.recalculate_area()

    def getSqrFt(self):

        return self._sqrFt

    def _calculateSqrFt(self, l, w):

        sqrFt = (l * w)
        return sqrFt

    def recalculateSqrFt(self):

        self._sqrFt = self._calculateSqrFt(self._length, self._width)

    def get_area(self):

        return self._area

    def _calculate_area(self, l, w, h):

        area = (l * w * h)
        return area

    def recalculate_area(self):

        self._area = self._calculate_area(self._length, self._width, self._height)

    def get_temp(self):

        return self._temp

    def set_temp(self, temp):

        self._temp = temp

    def change_temp(self, change):

        self._temp += change

    def get_rad(self):

        return self._rad

    def set_rad(self, rad):

        if isinstance(rad, Rad):
            self._rad = rad

    def get_door(self):

        return self._door

    def set_door(self, door):

        self._door = door

    def open_door(self):

        self._door.open_door()

    def close_door(self):

        self._door.close_door()

    def get_light(self):

        return self._light

    def set_light(self, light):

        self._light = light

    def get_window(self):

        return self._window

    def set_window(self, window):

        self._window = window

    def open_window(self):

        self._window.open_window()

    def close_window(self):

        self._window.close_window()


def test():
    w = Window(2)
    d = Door(2.0)
    l = Light(95)
    r = Rad(3000)
    r = Room("Living room", 12, 15, 10, 10.5, r, d, l, w)
    print(r.get_length())
    print(r.get_width())
    print(r.get_height())
    print(r.getSqrFt())
    print(r.get_area())

    r.set_length(9)
    r.set_width(15)
    r.set_height(12)

    print(r.get_length())
    print(r.get_width())
    print(r.get_height())
    print(r.getSqrFt())
    print(r.get_area())

    r.change_temp(-1)
    print(r.get_temp())

    print(r)


if __name__ == "__main__":
    test()
