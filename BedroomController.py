import Firebase


class BedroomController(object):

    def __init__(self, bedroom):
        self._bedroom = bedroom

        self._eb = self._bedroom.get_electric_blanket()
        self.eb_active = Firebase.get_eb_active()
        Firebase.set_eb_max(self._eb.get_max_level())
        if self.eb_active:
            self._eb.turn_on(Firebase.get_eb_level())

    def activate_eb(self):
        self.eb_active = True
        Firebase.set_eb_active(self.eb_active)
        self._eb.turn_on(int(Firebase.get_eb_level()))

    def deactivate_eb(self):
        self.eb_active = False
        Firebase.set_eb_active(self.eb_active)
        self._eb.turn_off()
