import unittest
from duel import unit, arena
from unittest import mock


class TestArena(unittest.TestCase):
	def setUp(self):
		self.unit1 = mock.Mock()
		self.unit2 = mock.Mock()
		self.ai_func = mock.Mock()
		self.arena = arena.Arena(self.unit1, self.unit2, self.ai_func)

	def testUpdate(self):
		self.arena.update()
		
		self.unit1.update.assert_called_once()
		self.unit2.update.assert_called_once()
		self.ai_func.assert_called_once_with(self.unit1, self.unit2)

	def testGuard(self):
		self.arena.guard(arena.PLAYER_1)
		self.arena.guard(arena.PLAYER_2)

		self.unit1.guard.assert_called_once()
		self.unit2.guard.assert_called_once()

	def testStopGuard(self):
		self.arena.stop_guard(arena.PLAYER_1)
		self.arena.stop_guard(arena.PLAYER_2)

		self.unit1.stop_guard.assert_called_once()
		self.unit2.stop_guard.assert_called_once()

	def testAttack(self):
		self.arena.attack(arena.PLAYER_1)
		self.arena.attack(arena.PLAYER_2)

		self.unit1.attack.assert_called_once()
		self.unit2.attack.assert_called_once()

	def testThrust(self):
		self.arena.thrust(arena.PLAYER_1)
		self.arena.thrust(arena.PLAYER_2)

		self.unit1.thrust.assert_called_once()
		self.unit2.thrust.assert_called_once()
