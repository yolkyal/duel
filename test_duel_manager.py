import unittest
from unittest import mock
import duel_manager, unit


class TestDuelManager(unittest.TestCase):
	def setUp(self):
		self.unit1 = mock.Mock()
		self.unit2 = mock.Mock()
		self.duel_manager = duel_manager.DuelManager(self.unit1, self.unit2)
	
	def testAttackNeutral(self):
		self.unit1.get_state.return_value = unit.STATE_ATTACK
		self.unit2.get_state.return_value = unit.STATE_NEUTRAL
		self.duel_manager.update()
		self.unit2.damage.assert_called_once()

		self.unit2.get_state.return_value = unit.STATE_ATTACK
		self.unit1.get_state.return_value = unit.STATE_NEUTRAL
		self.duel_manager.update()
		self.unit1.damage.assert_called_once()

	def testAttackDeflect(self):
		self.unit1.get_state.return_value = unit.STATE_ATTACK
		self.unit2.get_state.return_value = unit.STATE_DEFLECT
		self.duel_manager.update()
		self.unit1.deflect.assert_not_called()
		self.unit2.damage.assert_not_called()

		self.unit2.get_state.return_value = unit.STATE_ATTACK
		self.unit1.get_state.return_value = unit.STATE_DEFLECT
		self.duel_manager.update()
		self.unit2.deflect.assert_not_called()
		self.unit1.damage.assert_not_called()

	def testAttackGuard(self):
		self.unit1.get_state.return_value = unit.STATE_ATTACK
		self.unit2.get_state.return_value = unit.STATE_GUARD
		self.duel_manager.update()
		self.unit1.deflect.assert_not_called()
		self.unit2.damage.assert_not_called()

		self.unit2.get_state.return_value = unit.STATE_ATTACK
		self.unit1.get_state.return_value = unit.STATE_GUARD
		self.duel_manager.update()
		self.unit2.deflect.assert_not_called()
		self.unit1.damage.assert_not_called()

	def testThrustNeutral(self):
		self.unit1.get_state.return_value = unit.STATE_THRUST
		self.unit2.get_state.return_value = unit.STATE_NEUTRAL
		self.duel_manager.update()
		self.unit2.damage.assert_called_once()

		self.unit2.get_state.return_value = unit.STATE_THRUST
		self.unit1.get_state.return_value = unit.STATE_NEUTRAL
		self.duel_manager.update()
		self.unit1.damage.assert_called_once()

	def testThrustDeflect(self):
		self.unit1.get_state.return_value = unit.STATE_THRUST
		self.unit2.get_state.return_value = unit.STATE_DEFLECT
		self.duel_manager.update()
		self.unit1.deflect.assert_called_once()

		self.unit2.get_state.return_value = unit.STATE_THRUST
		self.unit1.get_state.return_value = unit.STATE_DEFLECT
		self.duel_manager.update()
		self.unit2.deflect.assert_called_once()

	def testThrustGuard(self):
		self.unit1.get_state.return_value = unit.STATE_THRUST
		self.unit2.get_state.return_value = unit.STATE_GUARD
		self.duel_manager.update()
		self.unit1.deflect.assert_not_called()
		self.unit2.damage.assert_called_once()

		self.unit2.get_state.return_value = unit.STATE_THRUST
		self.unit1.get_state.return_value = unit.STATE_GUARD
		self.duel_manager.update()
		self.unit2.deflect.assert_not_called()
		self.unit1.damage.assert_called_once()
