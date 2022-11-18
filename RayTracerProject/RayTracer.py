from cmath import pi, tan
from GL_library import *
from Vector import *
from light import Light 
from sphere import *
from material import *
from color import *
from plane import *
from envmap import *
from ambientLight import *

#Funciones y variables de utilidad
MAX_RECURSION_DEPTH = 3

def reflect(I, N): 
    return (I - N * 2 * (N @ I)).norm()

def refract(I, N, roi):
    etai = 1
    etat = roi
    
    cosi = (I @ N) * -1
    
    if (cosi < 0):
        cosi *= -1
        etai *= -1
        etat *= -1
        N *= -1

    eta = etai/etat
    k = (1 - ((eta ** 2) * (1 - (cosi ** 2))))
    
    if k < 0:
        return V3(0, 0, 0)
    
    cost = k ** 0.5
    
    return ((I * eta) + (N * ((eta * cosi) - cost))).norm()

class RayTracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height=height
        self.clear_color = Color(0,0,0) #Background color
        self.current_color=Color(255,255,255)
        self.scene=[]
        self.envmap = None
        self.ambientLight = None
        self.clear()
        
    def clear(self):
        self.framebuffer = [[self.clear_color for x in range(self.width)]
                            for y in range(self.height)]
        
    def point(self,x,y,color=None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = color or self.current_color
            
    def write(self, filename):
        Render.glFinish(self,filename)
    
    def render(self):
        fov=int(pi/2)
        ar=self.width/self.height
        for y in range(self.height):
            for x in range(self.width):
                i= (2*(x+0.5)/self.width-1)*tan(fov/2)*ar
                j= -(2*(y+0.5)/self.height-1)*tan(fov/2)
                direction=V3(i,j,-1).norm()
                origin= V3(0,0,0)
                c=self.cast_ray(origin,direction)
                #print("X: ", x)
                #print("Y: ", y)
                self.point(x,y,c)
                
        
    def cast_ray(self, origin, direction, recursion = 0):
        
        material, intersect = self.scene_intersect(origin, direction)
        
        if material is None or recursion >= MAX_RECURSION_DEPTH:
            if self.envmap:
                return self.envmap.getColor(direction)
            return self.clear_color
            # Si el rayo no golpeo nada o si llego al limite de recursion
        
        lightDir = (self.light.position - intersect.point).norm()
        lightDistance = V3.length(self.light.position - intersect.point)

        if self.ambientLight:
            ambientColor = self.ambientLight.color * self.ambientLight.strength
        else:
            ambientColor = self.clear_color
        
        offsetNormal = intersect.normal * 1.1
        shadowOrigin = intersect.point - offsetNormal if lightDir @ intersect.normal < 0 else intersect.point + offsetNormal
        shadowMaterial, shadowIntersect = self.scene_intersect(shadowOrigin, lightDir)
        shadowIntensity = 0

        if shadowMaterial and V3.length(shadowIntersect.point - shadowOrigin) < lightDistance:
            shadowIntensity = 0.9

        intensity = self.light.intensity * max(0, (lightDir @ intersect.normal)) * (1 - shadowIntensity)

        reflection = reflect(lightDir, intersect.normal)
        specularIntensity = self.light.intensity * (
            max(0, -(reflection @ direction)) ** material.spec
        )

        if material.albedo[2] > 0:
            reflectDir = reflect(direction, intersect.normal)
            reflectOrigin = (intersect.point - offsetNormal) if (reflectDir @ intersect.normal) < 0 else (intersect.point + offsetNormal)
            reflectedColor = self.cast_ray(reflectOrigin, reflectDir, recursion + 1)
        else:
            reflectedColor = self.currentColor

        if material.albedo[3] > 0:
            refractDir = refract(direction, intersect.normal, material.refractionIndex)
            refractOrigin = (intersect.point - offsetNormal) if (refractDir @ intersect.normal) < 0 else (intersect.point + offsetNormal)
            refractedColor = self.cast_ray(refractOrigin, refractDir, recursion + 1)
        else:
            refractedColor = self.clear_color

        diffuse = material.diffuse * intensity * material.albedo[0]
        specular = Color(255, 255, 255) * specularIntensity * material.albedo[1]
        reflected = reflectedColor * material.albedo[2]
        refracted = refractedColor * material.albedo[3]
        
        return ambientColor + diffuse + specular + reflected + refracted
        
     
    def scene_intersect(self, origin, direction):
        zbuffer = 999999
        material = None
        intersect = None
        for o in self.scene:
            object_intersect= o.ray_intersect(origin, direction)
            if object_intersect:
                if object_intersect.distance < zbuffer:
                    zbuffer=object_intersect.distance
                    material = o.material
                    intersect = object_intersect
        return material, intersect

#Probando la clase material
# red = Material(diffuse=Color(255,0,0))
# white = Material(diffuse=Color(255,255,0))
           
# r = RayTracer(800, 600)
# r.light = Light(position=V3(0,0,0),intensity=1)
# r.scene = [
#     Sphere(V3(-3,0,-16),2,red),
#     Sphere(V3(2.8,0,-10),2,white)]
# r.render()
# r.write('scene_intersect_prueba.bmp')
        
        
#Probando el envmap y el plano
r = RayTracer(800, 600)
r.envmap = Envmap('./envmap.bmp')
r.light = Light(V3(-10, 10, 1), 1, Color(255, 255, 255))

r.scene = [
    Sphere(V3(0, -1.5, -10), 1.5, Material(diffuse=Color(160,129,129), albedo=[0.6, 0.3, 0.1, 0], spec=50)),
    Sphere(V3(0, 0, -6), 0.5, Material(diffuse=Color(160,129,129), albedo=[0.6, 0.3, 0.1, 0], spec=50)),
    Sphere(V3(1, 1, -8), 1.7, Material(diffuse=Color(160,129,129), albedo=[0.6, 0.3, 0.1, 0], spec=50)),
    Sphere(V3(-2, 1, -10), 2, Material(diffuse=Color(160,129,129), albedo=[0.6, 0.3, 0.1, 0], spec=50)),
    Plane(V3(2, -10, -15), V3(0,1,0), Material(diffuse=Color(255, 255, 255), albedo=(0, 10, 0.8, 0), spec=1425, refractionIndex = 0))
]

r.render()
r.write('TestEnvmapPlane.bmp')

    
        