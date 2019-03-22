from Room import Room


class UtilityRoom(Room):

    def __init__(self, name, length, width, height, temp, rad, door, light, window, dryer):
        super().__init__(name, length, width, height, temp, rad, door, light, window)
        self._dryer = dryer

    def __str__(self):
        outstr = " " + str(self._dryer)
        return super().__str__() + outstr

    def get_dryer(self):
        return self._dryer

    def set_dryer(self, dryer):
        self._dryer = dryer
