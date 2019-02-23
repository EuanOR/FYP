from Room import Room
from Window import Window
class House(object):

    def __init__(self,insulation, rooms, lat, lon):
        
        if isinstance(insulation,bool):
            self._insulation = insulation
        else:
            self._insulation = False
            
        if (isinstance(rooms,list)):
            self._rooms = rooms
        else:
            self._rooms = []
        
        self._lat = lat
        self._lon = lon

        self._averageTemp = 0
        self.calculateAverageTemp()

    def insulate(self):
        
        print("House has been insulated")
        self._insulation = True
    
    def removeInsulation(self):

        self._insulation = False
        print("Insulation has been removed")
    
    def isInsulated(self):

        return self._insulation

    def getRooms(self):
        
        print("Rooms:" + str(len(self._rooms)))
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

    r1 = Room("Kitchen",12,10,8,10.7,True,w1)
    r2 = Room("Kitchen",12,10,8,11.1,True,w2)
    r3 = Room("Kitchen",12,10,8,10.3,True,w3)
    r4 = Room("Kitchen",12,10,8,10.9,True,w4)
    r5 = Room("Kitchen",12,10,8,11.3,True,w5)
    r6 = Room("Kitchen",12,10,8,11.7,True,w6)

    h = House(True, [r1, r2, r3],-25.004, 30.032)
    h.insulate()
    h.isInsulated()
    print(h.getRooms())
    h.setRooms(["Bedroom, Kitchen, Garage"])
    h.addRoom("Living room")
    print(h.getRooms())
    print(h.getLat())
    h.setLon(12.651)
    print(h.getLon())
    print(h.getAverageTemp())

if __name__ == "__main__":
    test()