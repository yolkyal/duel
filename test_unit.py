import unittest, time
import unit


class TestUnit(unittest.TestCase):
	def setUp(self):
		self.pos = (100, 100)
		self.dimensions = (100, 100)
		self.unit = unit.Unit(self.pos, self.dimensions)

	def testDefaults(self):
		self.assertEqual(unit.STATE_NEUTRAL, self.unit.get_state())

	def testGuard(self):
		self.unit.guard()
		self.assertEqual(unit.STATE_DEFLECT, self.unit.get_state())

		time.sleep(0.2)
		self.unit.update()
		self.assertEqual(unit.STATE_GUARD, self.unit.get_state())

		self.unit.stop_guard()
		self.assertEqual(unit.STATE_NEUTRAL, self.unit.get_state())

	def testAttack(self):
		self.unit.attack()
		self.assertEqual(unit.STATE_ATTACK_PREPARE, self.unit.get_state())

		time.sleep(0.3)
		self.unit.update()
		self.assertEqual(unit.STATE_ATTACK, self.unit.get_state())

		time.sleep(0.1)
		self.unit.update()
		self.assertEqual(unit.STATE_NEUTRAL, self.unit.get_state())

	def testThrust(self):
		self.unit.thrust()
		self.assertEqual(unit.STATE_THRUST_PREPARE, self.unit.get_state())

		time.sleep(0.5)
		self.unit.update()
		self.assertEqual(unit.STATE_THRUST, self.unit.get_state())

		time.sleep(0.3)
		self.unit.update()
		self.assertEqual(unit.STATE_NEUTRAL, self.unit.get_state())

	def testDamage(self):
		self.unit.damage()
		self.assertEqual(unit.STATE_DAMAGED, self.unit.get_state())

		time.sleep(0.3)
		self.unit.update()
		self.assertEqual(unit.STATE_NEUTRAL, self.unit.get_state())

	def testDeflect(self):
		self.unit.deflect()
		self.assertEqual(unit.STATE_DEFLECTED, self.unit.get_state())

		time.sleep(1)
		self.unit.update()
		self.assertEqual(unit.STATE_NEUTRAL, self.unit.get_state())

	def testRect(self):
		self.assertEqual((self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1]), self.unit.get_rect())
