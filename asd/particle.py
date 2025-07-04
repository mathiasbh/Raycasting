from ray import Ray
from pygame.draw import circle,line
from pygame.key import get_pressed
from pygame import K_p
import numpy as np



class Particle(object):
	"""docstring for Particle"""

	def __init__(self, screen, width, height, dir, fov):
		self.screen = screen
		self.pos = [width / 2, height / 2]
		self.dir = dir
		self.fov = fov
		self.rays = []


		for a in np.arange(-fov/2, fov/2, 2*fov/200):
			self.rays.append(Ray(self.screen, self.pos, a+self.dir))


	def updatePos(self, x, y):
		self.pos = [x, y]


	def updateDir(self, angle):
		self.dir += angle

		for ray in self.rays:
			ray.updateDir(angle)



	def look(self, walls):
		distscene = []

		for ray in self.rays:
			closest = None
			distiter = np.Inf

			for wall in walls:
				pt = ray.cast(wall)
				if pt:
					dist = np.sqrt((self.pos[0] - pt[0])**2 + (self.pos[1] - pt[1])**2)
					#dist *= np.cos(self.dir - ray.dir)

					if dist < distiter:
						distiter = dist
						closest = pt

			if closest:
				line(self.screen, (255,255,255), (self.pos[0], self.pos[1]), (closest[0], closest[1]), 1)

			# Vector of distances or lengths of rays to walls
			distscene.append(distiter) 
		return(distscene)

	def show(self):
		particle_size = 8

		circle(self.screen, (255,255,255), (int(self.pos[0]), int(self.pos[1])), particle_size, 0)

		for ray in self.rays:
			ray.updatePos(self.pos[0], self.pos[1])
			#ray.updateDir(self.dir)
			ray.show()


