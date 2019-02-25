from Controller import Controller
from Display import Display
from Heater import Heater
from House import House
from Monitor import Monitor
from Rad import Rad
from Room import Room
from Window import Window

import threading

class Main(object):

    livingRoomWindow = Window(3)
    livingRoomRad = Rad(3000)
    livingRoom = Room("Living Room",16,20,8,12.0,livingRoomRad,livingRoomWindow)

    kitchenWindow  = Window(1)
    kitchenRad = Rad(2000)
    kitchen = Room("Kitchen",10,16,8, 15.0, kitchenRad, kitchenWindow )  

    bedroom1Window = Window(3)
    bedroom1Rad = Rad(3000)
    bedroom1 = Room("Bedroom 1",12,12,8,9.0,bedroom1Rad,bedroom1Window)

    houseRooms = [livingRoom,kitchen,bedroom1]
    Home = House(True,houseRooms,"-37.8136","144.9631")

    Boiler = Heater(Home)

    Mon = Monitor(10,30,Boiler)

    c = Controller(Home,Mon)
    d = Display(Home,Boiler)
    def run(self):

        controller = threading.Thread(target = self.c.run)
        #display = threading.Thread(target = self.d.run)

        controller.start()
        #Calls a class that create a tkinter object to display the house in a seperate window
        #display.start()


if __name__ == "__main__":

    m = Main()
    m.run()
