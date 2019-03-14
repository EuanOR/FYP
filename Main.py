from Controller import Controller
from Door import Door
from Heater import Heater
from House import House
from Kettle import Kettle
from Kitchen import Kitchen
from KitchenController import KitchenController
from Light import Light
from LightController import LightController
from Monitor import Monitor
from Oven import Oven
from Rad import Rad
from Room import Room
from Toaster import Toaster
from Window import Window

import threading
#import tkinter

livingRoomWindow = Window(3)
livingRoomRad = Rad(3000)
livingRoomLight = Light(90)
livingRoomDoor = Door(1.5)
livingRoom = Room("Living Room", 16, 20, 8, 12.0, livingRoomRad, livingRoomDoor, livingRoomLight, livingRoomWindow)

kitchenWindow = Window(1)
kitchenRad = Rad(2000)
kitchenLight = Light(80)
kitchenDoor = Door(1.5)
kettle = Kettle(2, 100)
oven = Oven(280)
toaster = Toaster(8)
kitchen = Kitchen("Kitchen", 10, 16, 8, 12.0, kitchenRad, kitchenDoor, kitchenLight, kitchenWindow, \
                  kettle, oven, toaster)

bedroom1Window = Window(3)
bedroom1Rad = Rad(3000)
bedroom1Light = Light(98)
bedroom1Door = Door(1.5)
bedroom1 = Room("Bedroom 1", 12, 12, 8, 11.0, bedroom1Rad, bedroom1Door, bedroom1Light, bedroom1Window)

houseRooms = [livingRoom, kitchen, bedroom1]
houseRads = [livingRoomRad, kitchenRad, bedroom1Rad]
houseLights = [livingRoomLight, kitchenLight, bedroom1Light]
Boiler = Heater(houseRads)
Light_Controller = LightController(houseLights)
Kitchen_Controller = KitchenController(kitchen)
Home = House(True, houseRooms, Boiler, "-37.8136", "144.9631")

Mon = Monitor(0, 30, Boiler, Light_Controller, Kitchen_Controller)

c = Controller(Home, Mon)

c.run()