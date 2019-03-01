from Controller import Controller
from Display import Display
from Door import Door
from Heater import Heater
from House import House
from Monitor import Monitor
from Rad import Rad
from Room import Room
from Window import Window

import threading
import tkinter

livingRoomWindow = Window(3)
livingRoomRad = Rad(3000)
livingRoomDoor = Door(1.5)
livingRoom = Room("Living Room",16,20,8,12.0,livingRoomRad,livingRoomDoor,livingRoomWindow)

kitchenWindow  = Window(1)
kitchenRad = Rad(2000)
kitchenDoor = Door(1.5)
kitchen = Room("Kitchen",10,16,8, 15.0, kitchenRad, kitchenDoor,kitchenWindow )  

bedroom1Window = Window(3)
bedroom1Rad = Rad(3000)
bedroom1Door = Door(1.5)
bedroom1 = Room("Bedroom 1",12,12,8,9.0,bedroom1Rad,bedroom1Door,bedroom1Window)

houseRooms = [livingRoom,kitchen,bedroom1]
Boiler = Heater(houseRooms)
Home = House(True,houseRooms,Boiler,"-37.8136","144.9631")

Mon = Monitor(10,30,Boiler)

c = Controller(Home,Mon)
d = Display(Home,Boiler)


c.run()  