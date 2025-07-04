import pygame 
import sys
from random import randint
from boundary import Boundary
from particle import Particle
from numpy import isinf, pi, arctan


off = 10
width = 800
height = 800
fovVert = 20
fovHors = 30 * pi / 180
size = [width*2, height]
screen = pygame.display.set_mode(size)


def setup(pyscreen):
	# Initialize the game engine
	pygame.init()
 
	pygame.display.set_caption("Raycasting")
	pyscreen.fill((0,0,0))

	walls = []

	for w in range(0, 5):
		x1 = randint(off, width - off)
		x2 = randint(off, width - off)
		y1 = randint(off, height - off)
		y2 = randint(off, height - off)
		walls.append(Boundary(pyscreen, x1, y1, x2, y2))

	# Build outer edge walls
	walls.append(Boundary(pyscreen, off, off, off, height-off))
	walls.append(Boundary(pyscreen, off, off, width-off, off))
	walls.append(Boundary(pyscreen, width-off, off, width-off, height-off))
	walls.append(Boundary(pyscreen, off, height-off, width-off, height-off))

	particle = Particle(pyscreen, width, height, 0, fovHors)
	return(walls, particle)



def show3d(scenedist):
	i = 0
	distmax = width

	for scene in scenedist:
		t = width / len(scenedist)  # needs changing depending on distance
		distcolor = abs(scene*scene * 255 / distmax/distmax - 255)
		distheight = height * fovVert / scene

		if isinf(distcolor):
			distcolor = 0
			#distheight = height / 2


		# First two arguments: upper left corner x,y
		# Third argument: width
		# Fourth argument: 

		#sceneH / 2, w + 1, h
		#rectcoord = [width + i*t + t / 2, off + height/4 , t+1, height/2 - off*2 + distheight] 
		rectcoord = [width + i*t + t / 2,  height/30 + distheight,  t+2, off + 10*distheight] 


		pygame.draw.rect(screen, (distcolor,distcolor,distcolor), rectcoord, 0) 
		i += 1


	
def draw():
	walls, particle = setup(screen)

	running = True
	clock = pygame.time.Clock()



	while running is True:
		screen.fill((0,0,0))

		if pygame.key.get_pressed()[pygame.K_q]:
				pygame.quit()
				sys.exit()
				running = False
		if pygame.key.get_pressed()[pygame.K_a]:
				particle.updateDir(-pi/180 * 1)
		if pygame.key.get_pressed()[pygame.K_s]:
			particle.updateDir(pi/180 * 1)

		for event in pygame.event.get():
			pass
			

		for wall in walls:
			wall.show()


		# Move particle with mouse
		mousepos = pygame.mouse.get_pos()
		particle.updatePos(mousepos[0], mousepos[1])

		particle.show()
		distscene = particle.look(walls)
		
		show3d(distscene)

		# Update game
		pygame.display.update()
		clock.tick(60)
	return()
 


draw()

