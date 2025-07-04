from pygame.draw import line
from numpy import cos,sin

class Ray(object):
	"""docstring for Ray"""

	def __init__(self, screen, pos, dir):
		self.screen = screen
		self.pos = pos
		self.dir = dir


	def updatePos(self, x, y):
		self.pos = [x, y]


	def updateDir(self, angle):
		self.dir += angle


	def show(self):
		ray_length = 5

		line(self.screen, (255,255,255), 
			  (self.pos[0], self.pos[1]), 
			  (self.pos[0] + ray_length*cos(self.dir), self.pos[1] + ray_length*sin(self.dir)), 1)
		
		

	def cast(self, wall):
		# Line-line intersection https://en.wikipedia.org/wiki/Line-line_intersection

		# Wall coordinates (first line)
		x1 = wall.a[0]
		y1 = wall.a[1]
		x2 = wall.b[0]
		y2 = wall.b[1]

		# Ray coodinates (second line)
		x3 = self.pos[0]
		y3 = self.pos[1]
		x4 = self.pos[0] + cos(self.dir) * 500
		y4 = self.pos[1] + sin(self.dir) * 500

		den = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
		if den == 0:  # Parallel lines
			return

		t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / den
		u = -((x1 - x2)*(y1 - y3) - (y1 - y2)*(x1 - x3)) / den

		if (t > 0 and t < 1 and u > 0):
			return [x1 + t*(x2 - x1), y1 + t*(y2 - y1)]
		else:
			return

