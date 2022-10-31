import time

class TFSM:
	def __init__(self, start_state, transitions):
		self.state = start_state
		self.time_state_entered = time.time()
		self.input_transitions = [transition for transition in transitions if type(transition[1]) is str]
		self.time_transitions = [transition for transition in transitions if type(transition[1]) in [int, float]]

	def set_state(self, state):
		self.state = state
		self.time_state_entered = time.time()

	def input(self, input):
		for transition in self.input_transitions:
			if transition[0] == self.state and transition[1] == input:
				self.set_state(transition[2])
				break

	def update(self):
		time_in_state = time.time() - self.time_state_entered
		for transition in self.time_transitions:
			if transition[0] == self.state and time_in_state >= transition[1]:
				self.set_state(transition[2])
				break
