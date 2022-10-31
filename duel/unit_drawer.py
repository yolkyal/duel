class UnitDrawer:
	def __init__(self, state_image_map):
		self.state_image_map = state_image_map

	def draw(self, d_surf, unit):
		d_surf.blit(self.state_image_map[unit.get_state()], (unit.pos[0], unit.pos[1]))
