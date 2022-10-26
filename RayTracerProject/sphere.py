from ctypes import pointer
from intersect import *
from Vector import V3


class Sphere(object):
    def __init__(self, center,radius, material):
        self.center=center
        self.radius=radius
        self.material=material
        
    def ray_intersect(self, origin, direction):
        
        L= self.center - origin
        #Devuelve la magnitud de L
        #print(direction)
        #print("L: ", L)
        tca = L @ direction
        l=L.length()
        
        #print("Valor de l: ", l)
 
        d2 = l**2 - tca**2
        
        #Si d^2 es mayor al radio de la esfera se retorna falso
        if d2>self.radius**2:
            #print("False del radius")
            return None
        
        thc=(self.radius**2 - d2)**0.5
        
        t0=tca - thc
        t1=tca + thc
        
        #Miramos si queda afuera de la esfera
        if t0 < 0: 
            t0 = t1 
        if t0 < 0:  
            return None
        
        impact = origin + direction * t0
        normal_ = (impact - self.center).norm()
        
        return Intersect(
            distance=t0, 
            point = impact,
            normal = normal_)
        