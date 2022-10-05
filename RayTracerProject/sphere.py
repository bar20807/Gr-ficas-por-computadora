from cmath import sqrt

from Vector import V3


class Sphere(object):
    def __init__(self, center,radius):
        self.center=center
        self.radius=radius
        
    def ray_intersect(self, origin, direction):
        
        L= self.center - origin
        #Devuelve la magnitud de L
        #print(direction)
        #print("L: ", L)
        tca = L @ direction
        l=L.length()
        
        #print("Valor de l: ", l)
        print("Valor de tca: ", tca)
        print("Valor de radius: ", self.radius)
        
        d2 = l**2 - tca**2
        
        #Si d^2 es mayor al radio de la esfera se retorna falso
        if d2>self.radius**2:
            #print("False del radius")
            return False
        
        thc=(self.radius**2 - d2)**0.5
        
        t0=tca - thc
        t1=tca + thc
        
        #Miramos si queda afuera de la esfera
        if t0<0:
            t0=t1
        if t0>0:
            return False
        
        return True
        