from cmath import *
import struct
from GL_library import *
from Vector import *
from sphere import *
from material import *
from color import *

class Plane(object):
    def __init__(self, y, material):
        self.y = y
        self.material = material

    def ray_intersect(self, orig, direction):
        d = -(orig.y + self.y) / direction.y
        pt = orig + (direction * d)

        if d <= 0 or abs(pt.x) > 2 or pt.z > -5 or pt.z < -10:
            return None

        normal = V3(0, 1, 0)

        return Intersect(
        distance=d,
        point=pt,
        normal=normal
        )