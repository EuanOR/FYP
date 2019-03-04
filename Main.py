from Controller import Controller
from Display import Display
from Door import Door
from Heater import Heater
from House import House
from Light import Light
from LightController import LightController
from Monitor import Monitor
from Rad import Rad
from Room import Room
from Window import Window

import threading
import tkinter

livingRoomWindow = Window(3)
livingRoomRad = Rad(3000)
livingRoomLight = Light(90)
livingRoomDoor = Door(1.5)
livingRoom = Room("Living Room", 16, 20, 8, 12.0, livingRoomRad, livingRoomDoor, livingRoomLight, livingRoomWindow)

kitchenWindow  = Window(1)
kitchenRad = Rad(2000)
kitchenLight = Light(80)
kitchenDoor = Door(1.5)
kitchen = Room("Kitchen", 10, 16, 8, 15.0, kitchenRad, kitchenDoor, kitchenLight, kitchenWindow)

bedroom1Window = Window(3)
bedroom1Rad = Rad(3000)
bedroom1Light = Light(98)
bedroom1Door = Door(1.5)
bedroom1 = Room("Bedroom 1", 12, 12, 8, 9.0, bedroom1Rad, bedroom1Door, bedroom1Light, bedroom1Window)

houseRooms = [livingRoom, kitchen, bedroom1]
houseRads = [livingRoomRad, kitchenRad, bedroom1Rad]
houseLights = [livingRoomLight, kitchenLight, bedroom1Light]
Boiler = Heater(houseRads)
Light_Controller = LightController(houseLights)
Home = House(True, houseRooms, Boiler, "-37.8136", "144.9631")

Mon = Monitor(0, 30, Boiler, Light_Controller)

c = Controller(Home, Mon)
d = Display(Home, Boiler)

c.run()

root = tkinter.Tk()
root.title("Home Comforts-Control")
tkinter.Label(root, textvariable = str(House)).pack()
for r in Home.get_rooms():
    tkinter.Label(root, textvariable=str(r)).pack()
root.mainloop()