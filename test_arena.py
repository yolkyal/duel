import unittest
import unit, arena
from unittest import mock


class TestArena(unittest.TestCase):
	def setUp(self):
		self.unit1 = mock.Mock()
		self.unit2 = mock.Mock()
		self.ai_func = mock.Mock()
		self.arena = arena.Arena(self.unit1, self.unit2, self.ai_func)

	def testGuard(self):
		self.arena.guard(arena.PLAYER_1)
		self.unit1.guard.assert_called_once()

	def testStopGuard(self):
		self.arena.stop_guard(arena.PLAYER_1)
		self.unit1.stop_guard.assert_called_once()

	def testAttack(self):
		self.arena.attack(arena.PLAYER_1)
		self.unit1.attack.assert_called_once()

	def testThrust(self):
		self.arena.thrust(arena.PLAYER_1)
		self.unit1.thrust.assert_called_once()


if __name__ == '__main__':
	unittest.main()