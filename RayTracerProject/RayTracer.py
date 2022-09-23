from cmath import pi, tan
from gl import *
from Vector import * 
from sphere import *

class RayTracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height=height
        self.clear_color = color(0,0,0)
        self.current_color=color(1,1,1)  
        self.clear()
        
    def clear(self):
        self.framebuffer = [[self.clear_color for x in range(self.width)]
                            for y in range(self.height)]
        
    def point(self,x,y,c=None):
        if y>0 and y<self.height and x>0 and x<self.width:
            self.framebuffer[y][x] = c or self.current_color
    def write(self, filename):
        Render.glFinish(self,filename)
    def render(self):
        fov=int(pi/2)
        ar=self.width/self.height
        for y in range(self.height):
            for x in range(self.width):
                i= ((2*(x+0.5)/self.width)-1)*tan(fov/2)*ar
                j= -((2*(y+0.5)/self.height)-1)*tan(fov/2)
                direction=V3(i,j,-1).norm()
                origin= V3(0,0,0)
                c=self.cast_ray(origin,direction)
                #print("X: ", x)
                #print("Y: ", y)
                self.point(x,y,c)
        
    def cast_ray(self, origin, direction):
        s=Sphere(V3(-3,0,-16), 2)
        #Vemos si la esfera intersecta con la dirección y origen de la esfera
        #print("Valor arrojado por ray_intersect: ", s.ray_intersect(origin, direction))
        if s.ray_intersect(origin,direction):
            #print("color rojo")
            return color(1,0,0)
        else:
            #print("entre clearcolor")
            return self.clear_color

r = RayTracer(800,800)
r.render()
#r.point(100,100)
r.write('Sphere.bmp')
    
        