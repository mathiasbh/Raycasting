from pygame.draw import line
from numpy import cos,sin

class Ray(object):
	"""docstring for Ray"""

	def __init__(self, screen, pos, angle):
		self.screen = screen
		self.pos = pos
		self.angle = angle


	def update(self, x, y):
		self.pos = [x, y]



	def show(self):
		ray_length = 10

		line(self.screen, (255,155,155), 
			(self.pos[0], self.pos[1]), 
			(self.pos[0] + ray_length*cos(self.angle), self.pos[1] + ray_length*sin(self.angle)), 1)
		
		