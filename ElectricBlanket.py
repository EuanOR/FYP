class ElectricBlanket(object):

    def __init__(self, max_level):
        self._active = False
        self._cur_level = 1
        self._MAX_LEVEL = max_level

    def __str__(self):

        outstr = ""
        outstr += "Blanket:"
        if self._active:
            outstr += "On "

        else:
            outstr += "Off "
        outstr += ("Level:" + str(self._cur_level))
        return outstr

    def set_cur_level(self, level):

        if 0 < level <= self._MAX_LEVEL:
            self._cur_level = level
        else:
            print("Level cannot exceed" + str(self._MAX_LEVEL))

    def get_max_level(self):

        return self._MAX_LEVEL

    def turn_on(self, level):

        if 0 < level <= self._MAX_LEVEL:
            self._active = True
            self._cur_level = level
        else:
            print("Level cannot exceed %i"%(self._MAX_LEVEL))

    def turn_off(self):

        self._active = False
