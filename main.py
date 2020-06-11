import pygame, sys
import unit
from unit import Unit
from unit_drawer import UnitDrawer
from arena import Arena
from arena_drawer import ArenaDrawer
from arena_control import ArenaControl
from duel_manager import DuelManager
from image_manager import ImageManager

def ai_func(unit1, unit2):
	if unit1.get_state() == unit.STATE_NEUTRAL:
		unit2.stop_guard()
		unit2.attack()
	elif unit1.get_state() in (unit.STATE_GUARD, unit.STATE_DEFLECTED):
		unit2.stop_guard()
		unit2.thrust()
	elif unit1.get_state() in (unit.STATE_ATTACK_PREPARE, unit.STATE_THRUST_PREPARE):
		unit2.guard()

def main():
	image_manager = ImageManager()
	image_manager.store('images/background.png', 'BACKGROUND')
	image_manager.store('images/unit_neutral.png', 'NEUTRAL')
	image_manager.store('images/unit_guard.png', 'GUARD')
	image_manager.store('images/unit_attack.png', 'ATTACK')
	image_manager.store('images/unit_attack_prepare.png', 'ATTACK_PREPARE')
	image_manager.store('images/unit_thrust_prepare.png', 'THRUST_PREPARE')
	image_manager.store('images/unit_thrust.png', 'THRUST')
	image_manager.store('images/unit_deflected.png', 'DEFLECTED')
	image_manager.store('images/unit_damaged.png', 'DAMAGED')

	unit_drawer_1 = UnitDrawer({
		unit.STATE_NEUTRAL : image_manager.image('NEUTRAL').size((384, 288)).get(),
		unit.STATE_GUARD : image_manager.image('GUARD').size((384, 288)).get(), 
		unit.STATE_ATTACK : image_manager.image('ATTACK').size((384, 288)).get(), 
		unit.STATE_ATTACK_PREPARE : image_manager.image('ATTACK_PREPARE').size((384, 288)).get(),
		unit.STATE_THRUST_PREPARE : image_manager.image('THRUST_PREPARE').size((384, 288)).get(),
		unit.STATE_THRUST : image_manager.image('THRUST').size((384, 288)).get(),
		unit.STATE_DEFLECT : image_manager.image('GUARD').size((384, 288)).get(),
		unit.STATE_DEFLECTED : image_manager.image('DEFLECTED').size((384, 288)).get(),
		unit.STATE_DAMAGED : image_manager.image('DAMAGED').size((384, 288)).get()})

	unit_drawer_2 = UnitDrawer({
		unit.STATE_NEUTRAL : image_manager.image('NEUTRAL').size((384, 288)).flipped().get(),
		unit.STATE_GUARD : image_manager.image('GUARD').size((384, 288)).flipped().get(), 
		unit.STATE_ATTACK : image_manager.image('ATTACK').size((384, 288)).flipped().get(), 
		unit.STATE_ATTACK_PREPARE : image_manager.image('ATTACK_PREPARE').size((384, 288)).flipped().get(),
		unit.STATE_THRUST_PREPARE : image_manager.image('THRUST_PREPARE').size((384, 288)).flipped().get(),
		unit.STATE_THRUST : image_manager.image('THRUST').size((384, 288)).flipped().get(),
		unit.STATE_DEFLECT : image_manager.image('GUARD').size((384, 288)).flipped().get(),
		unit.STATE_DEFLECTED : image_manager.image('DEFLECTED').size((384, 288)).flipped().get(),
		unit.STATE_DAMAGED : image_manager.image('DAMAGED').size((384, 288)).flipped().get()})

	unit_1 = Unit((-20, 124), (384, 288))
	unit_2 = Unit((140, 124), (384, 288))
	arena = Arena(unit_1, unit_2, ai_func)
	arena_drawer = ArenaDrawer(unit_drawer_1, unit_drawer_2, image_manager.image('BACKGROUND').size((500, 500)).get())
	arena_control = ArenaControl(arena)
	duel_manager = DuelManager(unit_1, unit_2)

	pygame.init()
	pygame.display.set_caption('Duel')
	size = width, height = 500, 500
	d_surf = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	while True:
		delta_ms = clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			else:
				arena_control.handle_event(event)

		duel_manager.update()
		arena.update()

		clock.tick(30)
		arena_drawer.draw(d_surf, arena)
		pygame.display.update()

if __name__ == '__main__':
	main()
