class Window(object):

    def __init__(self, glazing):
        if 1 <= glazing <= 3:
            self._glazing = glazing
        elif glazing > 3:
            print("Windows cannot have more than triple glazing")
        else:
            print("Glazing cannot be less than one")
        
        self._open = False
    
    def get_glazing(self):
        
        return self._glazing
    
    def set_glazing(self, glazing):
        
        if 1 <= glazing <= 3:
            self._glazing = glazing
        elif glazing > 3:
            print("Windows cannot have more than triple glazing")
        else:
            print("Glazing cannot be less than one")
    
    def open_window(self):
        
        self._open = True
    
    def close_window(self):
        
        self._open = False
    
    def is_open(self):
        return self._open
