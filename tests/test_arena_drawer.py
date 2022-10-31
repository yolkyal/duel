import unittest
from unittest import mock
from duel import arena_drawer


class TestArenaDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()

		self.unit_drawer1 = mock.Mock()
		self.unit_drawer2 = mock.Mock()
		self.background_image = mock.Mock()
		self.arena_drawer = arena_drawer.ArenaDrawer(self.unit_drawer1, self.unit_drawer2, self.background_image)

		self.unit_1 = mock.Mock()
		self.unit_2 = mock.Mock()
		self.arena = mock.Mock()
		self.arena.unit_1 = self.unit_1
		self.arena.unit_2 = self.unit_2

	def testDraw(self):
		self.arena_drawer.draw(self.d_surf, self.arena)
		
		self.d_surf.blit.assert_called_once_with(self.background_image, (0, 0))
		self.unit_drawer1.draw.assert_called_once_with(self.d_surf, self.unit_1)
		self.unit_drawer2.draw.assert_called_once_with(self.d_surf, self.unit_2)
