from Room import Room


class Bedroom(Room):
    def __init__(self, name, length, width, height, temp, rad, door, light, window, electric_blanket):
        super().__init__(name, length, width, height, temp, rad, door, light, window)
        self._electric_blanket = electric_blanket

    def get_electric_blanket(self):

        return self._electric_blanket

    def set_electric_blanket(self, electric_blanket):

        self._electric_blanket = electric_blanket