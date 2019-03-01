from Room import Room
from Window import Window
from Door import Door
from Heater import Heater
class House(object):

    def __init__(self,insulation, rooms, heater, lat, lon):
        
        if isinstance(insulation,bool):
            self._insulation = insulation
        else:
            self._insulation = False
            
        if (isinstance(rooms,list)):
            self._rooms = rooms
        else:
            self._rooms = []
        
        self._heater = heater
        
        self._lat = lat
        self._lon = lon

        self._averageTemp = 0
        self.calculateAverageTemp()
    
    def __str__(self):

        outstr = "|House|"
        outstr += " "
        outstr += ("Average Temperature:" + str(self._averageTemp))
        outstr += " " 
        outstr += ("Rooms:" + str(len(self._rooms)))

        return outstr

    def insulate(self):
        
        print("House has been insulated")
        self._insulation = True
    
    def removeInsulation(self):

        self._insulation = False
        print("Insulation has been removed")
    
    def isInsulated(self):

        return self._insulation

    def getRooms(self):
        
        return self._rooms

    def setRooms(self, new_rooms):
        
        if(isinstance(new_rooms,list)):
            for r in new_rooms:
                if(not isinstance(r,Room)):
                    print("Get Here")
                    return "Must be an instance of the Room Class"
            self._rooms = new_rooms
        
        else:
            print("Invalid Operation: Must be of type list")
    
    def getHeater(self):

        return self._heater
    
    def setHeater(self, newHeater):

        if isinstance(newHeater,Heater):
            self._heater = newHeater
        
        else:
            print("Must be of type heater.")
    
    def addRoom(self, new_room):
        
        if (isinstance(new_room, Room)):
            self._rooms.append(new_room)
        else:
            print("Must be an instance of the Room Class")
    
    def getLat(self):
        
        return self._lat
    
    def setLat(self, new_lat):

        self._lat = new_lat
    
    def getLon(self):

        return self._lon
    
    def setLon(self, new_lon):

        self._lon = new_lon
    
    def getAverageTemp(self):
        
        return self._averageTemp
    
    def calculateAverageTemp(self):
        
        combinedTemp = 0
        for r in self._rooms:
            combinedTemp += r.getTemp()
        
        self._averageTemp = round(combinedTemp/(len(self._rooms)),2)

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

    r1 = Room("Kitchen",12,10,8,10.7,True,d1,w1)
    r2 = Room("Kitchen",12,10,8,11.1,True,d2,w2)
    r3 = Room("Kitchen",12,10,8,10.3,True,d3,w3)
    r4 = Room("Kitchen",12,10,8,10.9,True,d4,w4)
    r5 = Room("Kitchen",12,10,8,11.3,True,d5,w5)
    r6 = Room("Kitchen",12,10,8,11.7,True,d6,w6)

    b = Heater([r1,r2,r3])

    h = House(True, [r1, r2, r3],b,-25.004, 30.032)
    h.insulate()
    h.isInsulated()
    print(h.getRooms())
    h.setRooms([r4, r5, r6])
    h.addRoom("Living room")
    print(h.getRooms())
    print(h.getLat())
    h.setLon(12.651)
    print(h.getLon())
    print(h.getAverageTemp())

    print(h)

if __name__ == "__main__":
    test()