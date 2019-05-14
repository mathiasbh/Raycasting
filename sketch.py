import pygame 
import sys
from random import randint
from boundary import Boundary
from particle import Particle


off = 10
width = 800
height = 800
size = [width, height]
screen = pygame.display.set_mode(size)


def setup():
	# Initialize the game engine
	pygame.init()
 
	pygame.display.set_caption("Raycasting")
	screen.fill((0,0,0))

	walls = []

	for w in range(0, 6):
		x1 = randint(0, width)
		x2 = randint(0, width)
		y1 = randint(0, height)
		y2 = randint(0, height)
		walls.append(Boundary(screen, x1, y1, x2, y2))

	# Build outer edge walls
	walls.append(Boundary(screen, off, off, off, height-off))
	walls.append(Boundary(screen, off, off, width-off, off))
	walls.append(Boundary(screen, width-off, off, width-off, height-off))
	walls.append(Boundary(screen, off, height-off, width-off, height-off))

	particle = Particle(screen, width, height)
	return(walls, particle)


	

def draw():
	walls, particle = setup()

	running = True
	clock = pygame.time.Clock()



	while running is True:
		screen.fill((0,0,0))

		for event in pygame.event.get():
			if pygame.key.get_pressed()[pygame.K_q]:
				pygame.quit()
				sys.exit()


		for wall in walls:
			wall.show()

		# Move particle with mouse
		mousepos = pygame.mouse.get_pos()
		particle.update(mousepos[0], mousepos[1])
		
		particle.show()
		particle.look(walls)

		# Update game
		pygame.display.update()
		clock.tick(60)
	return()
 


draw()

