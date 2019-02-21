class House(object):

    def __init__(self,insulation, rooms, floors, lat, lon):
        
        if isinstance(insulation,bool):
            self._insulation = insulation
        else:
            self._insulation = False
            
        if (isinstance(rooms,list)):
            self._rooms = rooms
        else:
            self._rooms = []
        
        self._floors = floors
        self._lat = lat
        self._lon = lon

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
            self._rooms = new_rooms
        else:
            print("Invalid Operation: Must be of type list")
    
    def addRoom(self, new_room):
        
        self._rooms.append(new_room)
    
    def getLat(self):
        
        return self._lat
    
    def setLat(self, new_lat):

        self._lat = new_lat
    
    def getLon(self):

        return self._lon
    
    def setLon(self, new_lon):

        self._lon = new_lon

def test():

    h = House(True, ["room1, room2, room3"],2,-25.004, 30.032)
    h.insulate()
    h.isInsulated()
    print(h.getRooms())
    h.setRooms(["Bedroom, Kitchen, Garage"])
    h.addRoom("Living room")
    print(h.getRooms())
    print(h.getLat())
    h.setLon(12.651)
    print(h.getLon())

if __name__ == "__main__":
    test()