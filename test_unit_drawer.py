import unittest
from unittest import mock
import unit_drawer


class TestUnitDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()

		self.unit = mock.Mock()
		self.unit.pos = (100, 100)

		self.image_1 = mock.Mock()
		self.image_2 = mock.Mock()
		self.state_image_map = {0 : self.image_1, 1 : self.image_2}
		self.unit_drawer = unit_drawer.UnitDrawer(self.state_image_map)

	def testDraw1(self):
		# GIVEN
		self.unit.get_state.return_value = 0

		# WHEN
		self.unit_drawer.draw(self.d_surf, self.unit)

		# THEN
		self.d_surf.blit.assert_called_once_with(self.image_1, (self.unit.pos[0], self.unit.pos[1]))

	def testDraw2(self):
		# GIVEN
		self.unit.get_state.return_value = 1

		# WHEN
		self.unit_drawer.draw(self.d_surf, self.unit)

		# THEN
		self.d_surf.blit.assert_called_once_with(self.image_2, (self.unit.pos[0], self.unit.pos[1]))


if __name__ == '__main__':
	unittest.main()