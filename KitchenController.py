from Kettle import Kettle 
from Oven import Oven
from Toaster import Toaster

import Firebase


class KitchenController(object):

	def __init__(self, kitchen):

		self._kitchen = kitchen

		self._kettle = self._kitchen.get_kettle()
		self.kettle_active = Firebase.get_kettle_active()
		if self.kettle_active:
			self._kettle.boil()
			self._kettle_active = False

		self._oven = self._kitchen.get_oven()
		self.oven_active = Firebase.get_oven_active()
		if self.oven_active:
			self._oven.activate(int(Firebase.get_oven_temp()))

		self._toaster = self._kitchen.get_toaster()
		self.toaster_active = Firebase.get_toaster_active()
		if self.toaster_active:
			self._toaster.toast(int(Firebase.get_toaster_level()))

	def activate_kettle(self):
		self.kettle_active = True
		Firebase.set_kettle_active(self._kettle_active)
		self._kettle.boil()
		self.kettle_active = False
		Firebase.set_kettle_active(self._kettle_active)

	def activate_oven(self):

		self.oven_active = True
		Firebase.set_oven_active(self.oven_active)
		self._oven.activate(int(Firebase.get_oven_temp()))

	def deactivate_oven(self):
		self.oven_active = False
		Firebase.set_oven_active(self.oven_active)
		self._oven.deactivate()

	def activate_toaster(self):

		self.toaster_active = True
		Firebase.set_toaster_active(self.toaster_active)
		self._toaster.toast(int(Firebase.get_toaster_level()))

	def deactivate_toaster(self):

		self.toaster_active = False
		Firebase.set_toaster_active(self.toaster_active)
		self._toaster.turn_off()
