import pygame
import arena

DEFAULT_MOVE = 25

class ArenaControl:
	def __init__(self, arena):
		self.arena = arena

	def handle_event(self, e):
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_j:
				self.arena.attack(arena.PLAYER_1)
			elif e.key == pygame.K_k:
				self.arena.guard(arena.PLAYER_1)
			elif e.key == pygame.K_l:
				self.arena.thrust(arena.PLAYER_1)
		elif e.type == pygame.KEYUP:
			if e.key == pygame.K_k:
				self.arena.stop_guard(arena.PLAYER_1)
