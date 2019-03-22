import Firebase


class UtilityRoomController(object):

    def __init__(self, utility_room):
        self._utility_room = utility_room

        self._dryer = self._utility_room.get_dryer()
        self.dryer_active = Firebase.get_dryer_active()
        Firebase.set_dryer_max(int(self._dryer.get_max_temp()))
        if self.dryer_active:
            self._dryer.turn_on(Firebase.get_dryer_temperature())

    def activate_dryer(self):
        self.dryer_active = True
        Firebase.set_dryer_active(self.dryer_active)
        self._dryer.turn_on(Firebase.get_dryer_temperature())

    def deactivate_dryer(self):
        self.dryer_active = False
        Firebase.set_dryer_active(self.dryer_active)
        self._dryer.turn_off()
