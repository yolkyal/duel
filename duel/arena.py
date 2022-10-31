PLAYER_1 = 1
PLAYER_2 = 2


class Arena:
	def __init__(self, unit_1, unit_2, ai_func):
		self.unit_1 = unit_1
		self.unit_2 = unit_2
		self.ai_func = ai_func

	def update(self):
		self.unit_1.update()
		self.unit_2.update()
		self.ai_func(self.unit_1, self.unit_2)

	def attack(self, unit_id):
		if unit_id == PLAYER_1:
			self.unit_1.attack()
		elif unit_id == PLAYER_2:
			self.unit_2.attack()

	def guard(self, unit_id):
		if unit_id == PLAYER_1:
			self.unit_1.guard()
		elif unit_id == PLAYER_2:
			self.unit_2.guard()

	def stop_guard(self, unit_id):
		if unit_id == PLAYER_1:
			self.unit_1.stop_guard()
		elif unit_id == PLAYER_2:
			self.unit_2.stop_guard()

	def thrust(self, unit_id):
		if unit_id == PLAYER_1:
			self.unit_1.thrust()
		elif unit_id == PLAYER_2:
			self.unit_2.thrust()
