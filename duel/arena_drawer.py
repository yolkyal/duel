class ArenaDrawer:
	def __init__(self, unit_drawer1, unit_drawer2, background_image):
		self.unit_drawer1 = unit_drawer1
		self.unit_drawer2 = unit_drawer2
		self.background_image = background_image

	def draw(self, d_surf, arena):
		d_surf.blit(self.background_image, (0, 0))
		self.unit_drawer1.draw(d_surf, arena.unit_1)
		self.unit_drawer2.draw(d_surf, arena.unit_2)