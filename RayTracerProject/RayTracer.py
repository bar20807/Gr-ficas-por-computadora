from cmath import pi, tan
from GL_library import *
from Vector import *
from light import Light 
from sphere import *
from material import *
from color import *

def reflect(I, N): 
    return (I - N * 2 * (N @ I)).norm()

class RayTracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height=height
        self.clear_color = Color(0,0,0) #Background color
        self.current_color=Color(255,255,255)
        self.scene=[]
        self.light = Light(position=V3(0,0,0),intensity=1)
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
        
    def cast_ray(self, origin, direction):
        
        material, intersect = self.scene_intersect(origin, direction)
        
        if material is None:
            return self.clear_color
        
        light_dir = (self.light.position - intersect.point).norm()
        
        # Diffuse component
        diffuse_intensity = light_dir @ intersect.normal
        diffuse = material.diffuse * diffuse_intensity * material.albedo[0]
       
        # Specular component
        light_reflection = reflect(light_dir, intersect.normal)
        reflection_intensity = max(0, (light_reflection @ direction))
        specular_intensity = self.light.intensity * (reflection_intensity ** material.spec)
        specular = self.light.color * specular_intensity * material.albedo[1]

        return diffuse + specular
    
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
        
        


    
        