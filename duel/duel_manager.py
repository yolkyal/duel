from duel import unit

class DuelManager:
	def __init__(self, unit1, unit2):
		self.unit1 = unit1
		self.unit2 = unit2

	def update(self):
		for unit_pair in [(self.unit1, self.unit2), (self.unit2, self.unit1)]:
			if unit_pair[0].get_state() == unit.STATE_ATTACK:
				if unit_pair[1].get_state() not in (unit.STATE_GUARD, unit.STATE_DEFLECT):
					unit_pair[1].damage()
			elif unit_pair[0].get_state() == unit.STATE_THRUST:
				if unit_pair[1].get_state() == unit.STATE_DEFLECT:
					unit_pair[0].deflect()
				else:
					unit_pair[1].damage()