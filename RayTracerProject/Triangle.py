from GL_library import *
from Vector import *
from sphere import *
from material import *
from color import *
from plane import *
from envmap import *
from Cube import *

"""
    Referencias para armar la lógica del triangulo:
        https://www.scratchapixel.com/code.php?id=9&origin=/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle&src=0

"""

kEpsilon = 1e-8

class Triangle(object):
    def __init__(self, v0,v1,v2, material):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.material = material
        
    def ray_intersect(self, origin, direction):
        v0v1 = self.v1 - self.v0
        v0v2 = self.v2 - self.v0
        
        pvec = direction * v0v2
        det =  v0v1 @ pvec

        if  det > -kEpsilon and det < kEpsilon:
            return None
        
        invDet = 1 / det
        tvec = origin - self.v0
        
        u = (tvec @ pvec) * invDet
        
        if u < 0 or u > 1:
            return None
        
        qvec = tvec * v0v1
        v = (direction @ qvec) * invDet
        
        if v < 0 or u + v > 1:
            return None
        
        t = (v0v2 @ qvec) * invDet
        
        if t > kEpsilon:
            return Intersect(
                distance=t,
                point=origin + (direction * t),
                normal=(v0v1 * v0v2).norm()
            )
        else:
            return None
            
            
        
        
        
        

        
                
        
        
                
