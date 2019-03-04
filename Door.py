class Door(object):

    def __init__(self,thickness):

        if 1.0 < thickness < 3.0:
            self._thickness = thickness
        else:
            print("Door must be between 1 and 3 inches thick")
        
        self._open =  False
    
    def get_thickness(self):

        return self._thickness

    def set_thickness(self, thickness):

        if 1.0 < thickness < 3.0:

            self._thickness = thickness
        
        else:

            print("Door must be between 1 and 3 inches thick")

    def open_door(self):

        self._open = True
    
    def close_door(self):

        self._open =  False
    
    def is_open(self):

        return self._open