from ray import Ray
from pygame.draw import circle,line
import numpy as np


class Particle(object):
  """docstring for Particle"""

  def __init__(self, screen, width, height):
    self.screen = screen
    self.pos = [width / 2, height / 2]
    self.rays = []

    for a in np.arange(0, 2*np.pi, np.pi/90):
      self.rays.append(Ray(self.screen, self.pos, a))


  def update(self, x, y):
    self.pos = [x, y]


  def look(self, walls):
    for ray in self.rays:
      closest = None
      testdist = 10000


      for wall in walls:
        pt = ray.cast(wall)
        if pt:
          dist = np.sqrt((self.pos[0] - pt[0])**2 + (self.pos[1] - pt[1])**2)
          if dist < testdist:
            testdist = dist
            closest = pt


      if closest:
        #print(pt)
        #print(closest)
        line(self.screen, (255,255,0), (self.pos[0], self.pos[1]), (closest[0], closest[1]), 1)

        #print(pt)
        #something ray.cast(wall)


  def show(self):
    particle_size = 5

    circle(self.screen, (255,255,255), (int(self.pos[0]), int(self.pos[1])), particle_size, 0)

    for ray in self.rays:
      ray.update(self.pos[0], self.pos[1])
      ray.show()

