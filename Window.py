class Window(object):

    def __init__(self, glazing):
        if glazing >= 1 and glazing <= 3:
            self._glazing = glazing
        elif glazing > 3:
            print("Windows cannot have more than triple glazing")
        else:
            print("Glazing cannot be less than one")
        
        self._open = False
    
    def getGlazing(self):
        
        return self._glazing
    
    def setGlazing(self, new_glazing):
        
        if new_glazing >= 1 and new_glazing <=3:
            self._glazing = new_glazing
        elif new_glazing > 3:
            print("Windows cannot have more than triple glazing")
        else:
            print("Glazing cannot be less than one")
    
    def openWindow(self):
        
        self._open = True
    
    def closeWindow(self):
        
        self._open = False
    