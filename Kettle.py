import threading
import time

class Kettle(object):

    # IPS = Increase per second
    def __init__(self,  ips, boiling_point):

        self._ips = ips
        self._boiling_point = boiling_point

        self._cur_temp = 23

    def get_ips(self):

        return self._ips

    def set_ips(self, ips):

        self._ips = ips

    def get_boiling_point(self):

        return self._boiling_point

    def set_boiling_point(self, boiling_point):

        self._boiling_point = boiling_point

    def get_cur_temp(self):

        return self._cur_temp

    def increase_temp(self, increase):

        if isinstance(increase, int):
            self._cur_temp += increase

        else:
            print("Increase must be an integer value")

    def _boil(self):

        while self._cur_temp < self._boiling_point:
            self.increase_temp(self._ips)
            time.sleep(1)

        print(self._cur_temp)

    def boil(self):
        b = threading.Thread(target=self._boil)
        b.start()


def test():

    k = Kettle(2, 100)
    print(k.get_cur_temp())
    k.boil()

if __name__ == "__main__":

    test()
