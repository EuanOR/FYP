from Bedroom import Bedroom
from BedroomController import BedroomController
from Controller import Controller
from Door import Door
from Dryer import Dryer
from ElectricBlanket import  ElectricBlanket
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
from UtilityRoom import UtilityRoom
from UtilityRoomController import UtilityRoomController
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
oven = Oven(300)
toaster = Toaster(10)
kitchen = Kitchen("Kitchen", 10, 16, 8, 12.0, kitchenRad, kitchenDoor, kitchenLight, kitchenWindow, \
                  kettle, oven, toaster)

bedroom1Window = Window(3)
bedroom1Rad = Rad(2500)
bedroom1Light = Light(98)
bedroom1Door = Door(1.5)
electricBlanket = ElectricBlanket(5)
bedroom1 = Bedroom("Bedroom 1", 12, 12, 8, 12.0, bedroom1Rad, bedroom1Door, bedroom1Light, bedroom1Window, electricBlanket)

utilityRoomWindow = Window(3)
utilityRoomRad = Rad(1200)
utiilityRoomLight = Light(100)
utilityRoomDoor = Door(2)
dryer = Dryer(300)
utiilityRoom = UtilityRoom("Utility Room", 8,  8, 8, 12.0, \
    utilityRoomRad, utilityRoomDoor, utiilityRoomLight, utilityRoomWindow, dryer)

houseRooms = [livingRoom, kitchen, bedroom1, utiilityRoom]
houseRads = [livingRoomRad, kitchenRad, bedroom1Rad, utilityRoomRad]
houseLights = [livingRoomLight, kitchenLight, bedroom1Light, utiilityRoomLight]
Boiler = Heater(houseRads)
Light_Controller = LightController(houseLights)
Kitchen_Controller = KitchenController(kitchen)
Bedroom_Controller = BedroomController(bedroom1)
Utility_Room_Controller = UtilityRoomController(utiilityRoom)
Home = House(True, houseRooms, Boiler, "-37.8136", "144.9631")

Mon = Monitor(0, 30, Boiler, Light_Controller, Kitchen_Controller, Bedroom_Controller, Utility_Room_Controller)

c = Controller(Home, Mon)

c.run()