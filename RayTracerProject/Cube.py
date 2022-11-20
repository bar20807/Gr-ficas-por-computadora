from cmath import pi, tan
from GL_library import *
from Vector import V3
from light import Light 
from sphere import *
from material import *
from color import *
from plane import *
from envmap import *

"""
    Referencias para armar la lógica del cubo:
    https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-box-intersection
    https://inmensia.com/articulos/raytracing/planotrianguloycubo.html
    https://stackoverflow.com/questions/8903356/ray-tracing-box-intersections
"""


class Cubo(object): 
    def __init__(self, center, size, material):
        self.center = center
        self.size = size
        self.material = material

    def ray_intersect(self, origin, direction):
        tmin = float('-inf')
        tmax = float('inf')

        txmin = ((self.center.x - (self.size*0.5)) - origin.x) / direction.x
        txmax = ((self.center.x + (self.size*0.5)) - origin.x) / direction.x

        if txmin > txmax:
            txmin, txmax = txmax, txmin

        if txmin > tmin:
            tmin = txmin

        if txmax < tmax:
            tmax = txmax

        if tmin > tmax:
            return False

        tymin = ((self.center.y - (self.size*0.5)) - origin.y) / direction.y
        tymax = ((self.center.y + (self.size*0.5)) - origin.y) / direction.y

        if tymin > tymax:
            tymin, tymax = tymax, tymin

        if tymin > tmin:
            tmin = tymin

        if tymax < tmax:
            tmax = tymax

        if tmin > tmax:
            return False

        tzmin = ((self.center.z - (self.size*0.5)) - origin.z) / direction.z
        tzmax = ((self.center.z + (self.size*0.5)) - origin.z) / direction.z

        if tzmin > tzmax:
            tzmin, tzmax = tzmax, tzmin

        if tzmin > tmin:
            tmin = tzmin

        if tzmax < tmax:
            tmax = tzmax

        if tmin > tmax:
            return False

        if tmin < 0:
            tmin = tmax

            if tmin < 0:
                return False

        impact = (direction * tmin) - origin
        normal = (impact - self.center).norm()

        return Intersect(
            distance = tmin, 
            point = impact, 
            normal = normal,
        )