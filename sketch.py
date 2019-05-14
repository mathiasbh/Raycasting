import pygame 
import sys
from random import randint
from boundary import Boundary
from particle import Particle


xoff = 0
yoff = 10000
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

	for w in range(0, 5):
		x1 = randint(0, width)
		x2 = randint(0, width)
		y1 = randint(0, height)
		y2 = randint(0, height)
		walls.append(Boundary(screen, x1, y1, x2, y2))

	particle = Particle(screen, width, height)
	return(walls, particle)


	

def draw():
	walls, particle = setup()

	running = True
	clock = pygame.time.Clock()



	while running is True:
		screen.fill((0,0,0))

		for event in pygame.event.get():
			if event.type == pygame.key.get_pressed()[pygame.K_q]:
				print("HELLO, q pressed")
				#pygame.quit()
				#sys.exit()
				#print(event)

		for wall in walls:
			wall.show()

		# Move particle with mouse
		mousepos = pygame.mouse.get_pos()
		particle.update(mousepos[0], mousepos[1])
		particle.show()



		

		# Update game
		pygame.display.update()
		clock.tick(60)
	return()
 


draw()

