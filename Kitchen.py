from Room import Room


class Kitchen(Room):
    def __init__(self, name, length, width, height, temp, rad, door, light, window, kettle, toaster, oven):
        super().__init__(name, length, width, height, temp, rad, door, light, window)

        self._kettle = kettle
        self._toaster = toaster
        self._oven = oven

    # TODO Create getters and setters. STR Method.

    def get_kettle(self):

        return self._kettle

    def set_kettle(self, kettle):

        self._kettle = kettle

    def get_toaster(self):

        return self._toaster

    def set_toaster(self, toaster):

        self._toaster = toaster

    def get_oven(self):

        return self._oven

    def set_over(self, oven):

        self._oven = oven