from cmath import pi, tan
from GL_library import *
from Vector import *
from light import Light 
from sphere import *
from material import *
from color import *
from plane import *
from envmap import *
from Cube import *

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
        self.light = Light(V3(0, 0, 0), 2, Color(255,255,255))
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

    def background(self, direction):
        return self.envmap.getColor(direction) if (self.envmap is not None) else self.clear_color                               
    
    def cast_ray(self, origin, direction, recursion = 0):
        
        if recursion >= MAX_RECURSION_DEPTH:
            return self.background(direction)
        
        material, intersect = self.scene_intersect(origin, direction)
        
        if material is None:
            return self.background(direction)
        
        light_dir = (self.light.position - intersect.point).norm()
        
        # Shadow
        shadow_bias = 1.1
        shadow_orig = intersect.point + (intersect.normal * shadow_bias)
        shadow_material = self.scene_intersect(shadow_orig, light_dir)
        shadow_intensity = 0
        
        if shadow_material:
            shadow_intensity = 0.7
        
        # Diffuse component
        diffuse_intensity = light_dir @ intersect.normal
        diffuse = material.diffuse * diffuse_intensity * material.albedo[0] * (1 - shadow_intensity)
       
        # Specular component
        light_reflection = reflect(light_dir, intersect.normal)
        reflection_intensity = max(0, (light_reflection @ direction))
        specular_intensity = self.light.intensity * (reflection_intensity ** material.spec)
        specular = self.light.color * specular_intensity * material.albedo[1]
        
        # Reflection
        if material.albedo[2] > 0:
            reflect_direction = reflect(direction, intersect.normal)
            reflect_bias = -0.5 if reflect_direction @ intersect.normal < 0 else 0.5
            reflect_origin = intersect.point + (intersect.normal * reflect_bias) 
            reflect_color = self.cast_ray(reflect_origin, reflect_direction, recursion + 1)
        else:
            reflect_color = Color(0, 0, 0)
            
        reflection = reflect_color * material.albedo[2]
        
        # Refraction
        if material.albedo[3] > 0:
            refract_direction = refract(direction, intersect.normal, material.refractionIndex)
            refract_bias = -0.5 if ((refract_direction @ intersect.normal) < 0) else 0.5
            refract_origin = intersect.point + (intersect.normal * refract_bias) 
            refract_color = self.cast_ray(refract_origin, refract_direction, recursion + 1)
        else:
            refract_color = Color(0, 0, 0)
            
        refraction = refract_color * material.albedo[3]
        
        return diffuse + specular + reflection + refraction
        
     
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
# r = RayTracer(800, 800)
# r.envmap = Envmap('./envmap.bmp')
# r.light = Light(V3(-11, 11, 2), 2, Color(255, 255, 255))

# r.scene = [
#     Sphere(V3(0, -2, -11), 2, Material(diffuse=Color(255,255,255), albedo=[0.7, 0.4, 0.2, 0], spec=60)),
#     Sphere(V3(0, 0, -7), 1, Material(diffuse=Color(160,170,210), albedo=[0, 0.6, 0, 0.9], spec=126, refractionIndex=2))
# ]

# r.render()
# r.write('TestEnvmapPlane.bmp')

    
#Probando las piramides
# r = RayTracer(800, 800)
# r.envmap = Envmap('./envmap.bmp')
# r.light = Light(V3(-11, 11, 2), 2, Color(255, 255, 255))

# r.scene = [
#     Pyramid([(3, -1.4, -8.5), (1.9, -0.1, -8.5), (0.8, -1.4, -8.5), (2.5, -1, -10)], Material(diffuse = color(0.259, 0.412, 0.184),albedo=[0.7, 0.4, 0.2, 0], spec = 16))
# ]

# r.render()
# r.write('PyramidTest.bmp')

#Probando los cubos
# r = RayTracer(800, 800)
# r.envmap = Envmap('./envmap.bmp')
# r.light = Light(V3(-11, 11, 2), 2, Color(255, 255, 255))

# r.scene = [
#     Cubo(V3(0, 0, -7),2, Material(diffuse=Color(160,170,210), albedo = [0,0.6,0,0.9], spec = 126, refractionIndex=2))
# ]

# r.render()
# r.write('CubeTest.bmp')