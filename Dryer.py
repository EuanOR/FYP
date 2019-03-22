class Dryer(object):

    def __init__(self, max_temp):
        self._active = False
        self._cur_temp = 0
        self._MAX_TEMP = max_temp

    def __str__(self):
        outstr = ""
        outstr += "Dryer:"
        if self._active:
            outstr += "On "
        else:
            outstr += "Off "
        outstr += ("Temperature:" + str(self._cur_temp))
        return outstr

    def turn_on(self, temp):
        if 0 < temp < self._MAX_TEMP:
            self._active = True
            self._cur_temp = temp

        else:
            print("Dryer temperature cannot be set to any higher than "
                  + str(self._MAX_TEMP))

    def turn_off(self):

        self._active = False
        self._cur_temp = 0

    def get_max_temp(self):

        return self._MAX_TEMP