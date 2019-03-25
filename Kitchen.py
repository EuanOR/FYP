from Room import Room


class Kitchen(Room):
    def __init__(self, name, length, width, height, temp, rad, door, light, window, kettle, oven, toaster):
        super().__init__(name, length, width, height, temp, rad, door, light, window)

        self._kettle = kettle
        self._oven = oven
        self._toaster = toaster
        
    def __str__(self):
        outstr = " "
        outstr += str(self._kettle) + " "
        outstr += str(self._oven) + " "
        outstr += str(self._toaster) + " "
        return super().__str__() + outstr 

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

    def set_oven(self, oven):

        self._oven = oven