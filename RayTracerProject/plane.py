from cmath import *
import struct
from GL_library import *
from Vector import *
from sphere import *
from material import *
from color import *

class Plane(object):
    def __init__(self, position, normal, material):
        self.position = position
        self.normal =  normal.norm()
        self.material = material

    def ray_intersect(self, orig, dir):
        denom = dir @ self.normal
        if abs(denom) > 0.0001:
            t = (self.normal @ (self.position - orig)) / denom
            if t > 0:
                # P = O + tD
                hit = orig + (dir*t)

                return Intersect(distance = t,
                                 point = hit,
                                 normal = self.normal)

        return None