from cmath import *
import struct
from GL_library import *
from Vector import *
from sphere import *
from material import *
from color import *

class Plane(object):
    def __init__(self, center, width, large, material):
        self.center = center
        self.width = width
        self.large = large
        self.material = material
        
    def ray_intersect(self, origin, direction):
        d = (origin.y + self.center.y) / direction.y
        impact = origin + (direction * d)
        normal = V3(0, 1, 0)
        
        if (d <= 0) or \
            impact.x > (self.center.x + self.width/2) or impact.x < (self.center.x - self.width/2) or \
            impact.z > (self.center.z + self.large/2) or impact.z < (self.center.z - self.large/2): 
            return None
        
        return Intersect(
            distance=d,
            point=impact,
            normal=normal
        )