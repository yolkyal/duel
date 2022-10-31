import unittest, time
from duel import tfsm


class TestTFSM(unittest.TestCase):
	def testInputTransitions(self):
		fsm = tfsm.TFSM([('s1', 'input1', 's2'), ('s2', 'input2', 's1')])

		self.assertEqual('s1', fsm.state)

		fsm.input('input1')
		self.assertEqual('s2', fsm.state)

		fsm.input('input2')
		self.assertEqual('s1', fsm.state)

		fsm.input('input3')
		self.assertEqual('s1', fsm.state)

	def testTimeTransitions(self):
		fsm = tfsm.TFSM([('s1', '0.1', 's2'), ('s2', '0.2', 's1')])

		self.assertEqual('s1', fsm.state)

		time.sleep(0.2)
		fsm.update()
		self.assertEqual('s2', fsm.state)

		time.sleep(0.2)
		fsm.update()
		self.assertEqual('s1', fsm.state)
