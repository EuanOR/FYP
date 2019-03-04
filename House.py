from Room import Room
from Window import Window
from Door import Door
from Heater import Heater


class House(object):
    def __init__(self, insulation, rooms, heater, lat, lon):

        if isinstance(insulation, bool):
            self._insulation = insulation
        else:
            self._insulation = False

        if isinstance(rooms, list):
            self._rooms = rooms
        else:
            self._rooms = []

        self._heater = heater

        self._lat = lat
        self._lon = lon

        self.average_temp = 0
        self.calculate_average_temp()

    def __str__(self):

        outstr = "|House|"
        outstr += " "
        outstr += ("Average Temperature:" + str(self.average_temp))
        outstr += " "
        outstr += ("Rooms:" + str(len(self._rooms)))

        return outstr

    def insulate(self):

        print("House has been insulated")
        self._insulation = True

    def remove_insulation(self):

        self._insulation = False
        print("Insulation has been removed")

    def is_insulated(self):

        return self._insulation

    def get_rooms(self):

        return self._rooms

    def set_rooms(self, rooms):

        if isinstance(rooms, list):
            for r in rooms:
                if not isinstance(r, Room):
                    print("Get Here")
                    return "Must be an instance of the Room Class"
            self._rooms = rooms

        else:
            print("Invalid Operation: Must be of type list")

    def get_heater(self):

        return self._heater

    def set_heater(self, heater):

        if isinstance(heater, Heater):
            self._heater = heater

        else:
            print("Must be of type heater.")

    def add_room(self, new_room):

        if (isinstance(new_room, Room)):
            self._rooms.append(new_room)
        else:
            print("Must be an instance of the Room Class")

    def get_lat(self):

        return self._lat

    def set_lat(self, lat):

        self._lat = lat

    def get_lon(self):

        return self._lon

    def set_lon(self, lon):

        self._lon = lon

    def get_average_temp(self):

        return self.average_temp

    def calculate_average_temp(self):

        combined_temp = 0
        for r in self._rooms:
            combined_temp += r.get_temp()

        self.average_temp = round(combined_temp / (len(self._rooms)), 2)


def test():
    w1 = Window(2)
    w2 = Window(2)
    w3 = Window(2)
    w4 = Window(2)
    w5 = Window(2)
    w6 = Window(2)

    d1 = Door(1.5)
    d2 = Door(1.5)
    d3 = Door(1.5)
    d4 = Door(1.5)
    d5 = Door(1.5)
    d6 = Door(1.5)

    r1 = Room("Kitchen", 12, 10, 8, 10.7, True, d1, w1)
    r2 = Room("Kitchen", 12, 10, 8, 11.1, True, d2, w2)
    r3 = Room("Kitchen", 12, 10, 8, 10.3, True, d3, w3)
    r4 = Room("Kitchen", 12, 10, 8, 10.9, True, d4, w4)
    r5 = Room("Kitchen", 12, 10, 8, 11.3, True, d5, w5)
    r6 = Room("Kitchen", 12, 10, 8, 11.7, True, d6, w6)

    b = Heater([r1, r2, r3])

    h = House(True, [r1, r2, r3], b, -25.004, 30.032)
    h.insulate()
    h.is_insulated()
    print(h.get_rooms())
    h.set_rooms([r4, r5, r6])
    h.add_room("Living room")
    print(h.get_rooms())
    print(h.get_lat())
    h.set_lon(12.651)
    print(h.get_lon())
    print(h.get_average_temp())

    print(h)


if __name__ == "__main__":
    test()
