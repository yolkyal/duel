import unittest, pygame
from unittest import mock
from duel import arena, arena_control


class ArenaControlTest(unittest.TestCase):
	def setUp(self):
		self.arena = mock.Mock()
		self.arena_control = arena_control.ArenaControl(self.arena)

	def testAttack(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_j)
		self.arena_control.handle_event(e)
		self.arena.attack.assert_called_once_with(arena.PLAYER_1)

	def testGuard(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_k)
		self.arena_control.handle_event(e)
		self.arena.guard.assert_called_once_with(arena.PLAYER_1)

	def testStopGuard(self):
		e = pygame.event.Event(pygame.KEYUP, key=pygame.K_k)
		self.arena_control.handle_event(e)
		self.arena.stop_guard.assert_called_once_with(arena.PLAYER_1)

	def testThrust(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_l)
		self.arena_control.handle_event(e)
		self.arena.thrust.assert_called_once_with(arena.PLAYER_1)
