import unittest
import unit
from unittest import mock

class TestUnit(unittest.TestCase):
	def setUp(self):
		self.pos = (100, 100)
		self.dimensions = (100, 100)
		self.tfsm = mock.Mock()
		self.unit = unit.Unit(self.pos, self.dimensions, self.tfsm)

	def testGuard(self):
		self.unit.guard()
		self.tfsm.input.assert_called_with(unit.ACTION_GUARD)

	def testAttack(self):
		self.unit.attack()
		self.tfsm.input.assert_called_with(unit.ACTION_ATTACK)

	def testThrust(self):
		self.unit.thrust()
		self.tfsm.input.assert_called_once_with(unit.ACTION_THRUST)

	def testDamage(self):
		self.unit.damage()
		self.tfsm.set_state.assert_called_once_with(unit.STATE_DAMAGED)

	def testDeflect(self):
		self.unit.deflect()
		self.tfsm.set_state.assert_called_once_with(unit.STATE_DEFLECTED)

	def testRect(self):
		self.assertEqual((self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1]), self.unit.get_rect())
