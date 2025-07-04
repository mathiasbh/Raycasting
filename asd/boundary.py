from pygame.draw import line

class Boundary(object):
	"""docstring for Boundary"""

	def __init__(self, screen, x1, y1, x2, y2):
		self.screen = screen
		self.a = [x1, y1]
		self.b = [x2, y2]
		
	def show(self):
		line(self.screen, (255,255,255), (self.a[0], self.a[1]), (self.b[0], self.b[1]), 1)
