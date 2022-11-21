from GL_library import *
from Vector import *
from sphere import *
from material import *
from color import *
from envmap import *

kEpsilon = 1e-8

class Pyramid(object):
    def __init__(self, arrVectors, material):
        self.arrVectors = arrVectors
        self.material = material 
        
    def side(self, v0, v1, v2, origin, direction):
        
        v0v1 = v1 - v0
        v0v2 = v2 - v0
        
        N = v0v1 * v0v2
        
        ray_direction = N @ direction
        
        if ray_direction < kEpsilon:
            return None
        
        d = N @ v0

        t = (N @ origin + d) / ray_direction
        
        # print("Tipo de d: " + str(type(d)))
        
        # print("Tipo de N: " + str(type(N)))
        
        # print("Tipo de origin: " + str(type(origin)))
        
        # print("Tipo de direction: " + str(type(direction)))
        
        # print("Tipo de ray_direction: " + str(type(ray_direction)))
        
        if t < 0:
            return None
        
        P = origin + (direction * t)
        U,V,W = barycentric(v0,v1,v2,P)
        
        if U < 0 or V < 0 or W < 0:
            return None
        else:
            return Intersect(
                distance=t,
                point=P,
                normal=N.norm()
            )
    
    def ray_intersect(self, origin, direction):
        v0,v1,v2,v3 =  self.arrVectors
        
        sides = [
            self.side(v0,v2,v1,origin,direction),
            self.side(v0,v2,v3,origin,direction),
            self.side(v0,v3,v1,origin,direction),
            self.side(v1,v2,v3,origin,direction)
        ]
        
        t = float('inf')
        intersect = None
        
        for side in sides:
            if side is not None:
                if side.distance < t:
                    t = side.distance
                    intersect = side
        
        if intersect is None:
            return None
        
        return Intersect(distance = intersect.distance,
                         point = intersect.point,
                         normal = intersect.normal) 
                
        