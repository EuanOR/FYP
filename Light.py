class Light(object):

    def __init__(self,brightness):
        self._brightness = brightness
        self._on = False
    
    def getBrightness(self):

        return self._brightness
    
    def setBrightness(self, brightness):
        
        if (brightness > 0 and brightness <= 100):
            self._brightness = brightness
        else:
            print("Must be between 1-100")
    
    def turnOn(self):

        self._on = True
    
    def turnOff(self):

        self._on = False
    
    def isOn(self):

        return self._on