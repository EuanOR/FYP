class Light(object):

    def __init__(self,brightness):
        self._brightness = brightness
        self._on = False
    
    def get_brightness(self):

        return self._brightness
    
    def set_brightness(self, brightness):
        
        if 0 < brightness <= 100:
            self._brightness = brightness
        else:
            print("Must be between 1-100")
    
    def turn_on(self):

        self._on = True
    
    def turn_off(self):

        self._on = False
    
    def is_on(self):

        return self._on