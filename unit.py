import tfsm

STATE_NEUTRAL = 0
STATE_ATTACK = 1
STATE_GUARD = 2
STATE_ATTACK_PREPARE = 3
STATE_THRUST_PREPARE = 4
STATE_THRUST = 5
STATE_DEFLECT = 6
STATE_DEFLECTED = 7
STATE_DAMAGED = 8

ATTACK = 'ATTACK'
GUARD = 'GUARD'
STOP_GUARD = 'STOP_GUARD'
THRUST = 'THRUST'


STATE_TRANSITIONS = [(STATE_NEUTRAL, ATTACK, STATE_ATTACK_PREPARE), 
			(STATE_ATTACK_PREPARE, 0.3, STATE_ATTACK),
			(STATE_ATTACK, 0.1, STATE_NEUTRAL),
			(STATE_NEUTRAL, THRUST, STATE_THRUST_PREPARE), 
			(STATE_THRUST_PREPARE, 0.3, STATE_THRUST),
			(STATE_THRUST, 0.3, STATE_NEUTRAL),
			(STATE_NEUTRAL, GUARD, STATE_DEFLECT),
			(STATE_DEFLECT, 0.1, STATE_GUARD),
			(STATE_DEFLECT, STOP_GUARD, STATE_NEUTRAL),
			(STATE_GUARD, STOP_GUARD, STATE_NEUTRAL), 
			(STATE_DEFLECTED, 1, STATE_NEUTRAL),
			(STATE_DAMAGED, 0.3, STATE_NEUTRAL)]


class Unit:
	def __init__(self, pos, dimensions):
		self.pos = pos
		self.dimensions = dimensions
		self.tfsm = tfsm.TFSM(STATE_NEUTRAL, STATE_TRANSITIONS)

	def update(self):
		self.tfsm.update()

	def attack(self):
		self.tfsm.input(ATTACK)

	def guard(self):
		self.tfsm.input(GUARD)

	def stop_guard(self):
		self.tfsm.input(STOP_GUARD)

	def thrust(self):
		self.tfsm.input(THRUST)

	def deflect(self):
		self.tfsm.set_state(STATE_DEFLECTED)

	def damage(self):
		self.tfsm.set_state(STATE_DAMAGED)

	def get_state(self):
		return self.tfsm.state

	def get_rect(self):
		return (self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1])