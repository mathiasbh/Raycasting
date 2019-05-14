from ray import Ray
from pygame.draw import circle
import numpy as np


class Particle(object):
  """docstring for Particle"""

  def __init__(self, screen, width, height):
    self.screen = screen
    self.pos = [width / 2, height / 2]
    self.rays = []

    for a in np.arange(0, 2*np.pi, np.pi/45):
      self.rays.append(Ray(self.screen, self.pos, a))


  def update(self, x, y):
    self.pos = [x, y]


  def look(self, walls):
    pass

    
  def show(self):
    particle_size = 5
    
    circle(self.screen, (255,255,255), (int(self.pos[0]), int(self.pos[1])), particle_size, 0)

    for ray in self.rays:
      ray.update(self.pos[0], self.pos[1])
      ray.show()

