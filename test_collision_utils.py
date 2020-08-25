import unittest
import collision_utils


class TestCollisionUtils(unittest.TestCase):
	def testRectPtCollision(self):
		rect = (100, 100, 10, 10)

		# CENTRE
		self.assertTrue(collision_utils.is_rect_pt_collision(rect, (105, 105)))

		# CORNERS
		self.assertTrue(collision_utils.is_rect_pt_collision(rect, (100, 100)))
		self.assertFalse(collision_utils.is_rect_pt_collision(rect, (100, 99)))
		self.assertFalse(collision_utils.is_rect_pt_collision(rect, (99, 100)))

		# CORNERS
		self.assertTrue(collision_utils.is_rect_pt_collision(rect, (100, 110)))
		self.assertFalse(collision_utils.is_rect_pt_collision(rect, (100, 111)))
		self.assertFalse(collision_utils.is_rect_pt_collision(rect, (111, 100)))

		# CORNERS
		self.assertTrue(collision_utils.is_rect_pt_collision(rect, (110, 100)))
		self.assertFalse(collision_utils.is_rect_pt_collision(rect, (110, 99)))
		self.assertFalse(collision_utils.is_rect_pt_collision(rect, (111, 100)))

		# CORNERS
		self.assertTrue(collision_utils.is_rect_pt_collision(rect, (110, 110)))
		self.assertFalse(collision_utils.is_rect_pt_collision(rect, (111, 110)))
		self.assertFalse(collision_utils.is_rect_pt_collision(rect, (110, 111)))
