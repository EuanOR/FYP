class Oven(object):

    def __init__(self, max_temp):
        self._active = False
        self._cur_temp = 0
        self._MAX_TEMP = max_temp

    def __str__(self):
        outstr = ""
        outstr += "Oven:"
        if self._active:
            outstr += "On "
        else:
            outstr += "Off "
        outstr += ("Temperature:" + str(self._cur_temp))

        return outstr

    def get_max_temp(self):

        return self._MAX_TEMP

    def activate(self, temp):

        if temp <= self._MAX_TEMP:
            self._active = True
            self._cur_temp = temp

        else:
            print("Ovens temperature cannot be set to any higher than "
                  + str(self._MAX_TEMP))

    def deactivate(self):

        self._active = False
        self._cur_temp = 0


def test():
    ov = Oven(240)

    ov.activate(180)
    print(ov)
    ov.deactivate()
    print(ov)
    ov.activate(300)
    print(ov)

if __name__ == "__main__":

    test()