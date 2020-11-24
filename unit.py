STATE_NEUTRAL = 'STATE_NEUTRAL'
STATE_ATTACK_PREPARE = 'STATE_ATTACK_PREPARE'
STATE_ATTACK = 'STATE_ATTACK'
STATE_THRUST_PREPARE = 'STATE_THRUST_PREPARE'
STATE_THRUST = 'STATE_THRUST'
STATE_GUARD = 'STATE_GUARD'
STATE_DEFLECT = 'STATE_DEFLECT'
STATE_DEFLECTED = 'STATE_DEFLECTED'
STATE_DAMAGED = 'STATE_DAMAGED'

ACTION_ATTACK = 'ACTION_ATTACK'
ACTION_THRUST = 'ACTION_THRUST'
ACTION_GUARD = 'ACTION_GUARD'
ACTION_STOP_GUARD = 'ACTION_STOP_GUARD'

class Unit:
	def __init__(self, pos, dimensions, tfsm):
		self.pos = pos
		self.dimensions = dimensions
		self.tfsm = tfsm

	def update(self):
		self.tfsm.update()

	def attack(self):
		self.tfsm.input(ACTION_ATTACK)

	def guard(self):
		self.tfsm.input(ACTION_GUARD)

	def stop_guard(self):
		self.tfsm.input(ACTION_STOP_GUARD)

	def thrust(self):
		self.tfsm.input(ACTION_THRUST)

	def deflect(self):
		self.tfsm.set_state(STATE_DEFLECTED)

	def damage(self):
		self.tfsm.set_state(STATE_DAMAGED)

	def get_state(self):
		return self.tfsm.state

	def get_rect(self):
		return (self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1])