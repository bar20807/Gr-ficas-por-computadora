import struct as st
from GL_library import *
class Texture:
    def __init__(self,path):
        self.path=path
        self.read()
        
    def read(self):
        with open(self.path,"rb") as image:
            image.seek(2+4+2+2)
            #Lee un total de 4 bites
            #unpack sirve para darle un valor entero a los bites
            header_size=st.unpack("=l",image.read(4))[0]
            image.seek(2+4+2+2+4+4)
            #Creamos el ancho y alto de la imagen
            self.width=st.unpack("=l",image.read(4))[0]
            self.height=st.unpack("=l",image.read(4))[0]
            
            #Ahora leemos dicho archivo            
            image.seek(header_size)
            
            self.pixels=[]
            
            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b=ord(image.read(1))
                    g=ord(image.read(1))
                    r=ord(image.read(1))
                    self.pixels[y].append(
                        color((r/255),(g/255),(b/255))
                    )
    #Tomamos el color que se encuentra en cierta posición de nuestro array
    def get_color(self,tx,ty):
        x= round(tx*self.width)
        y= round(ty*self.height)
        
        return self.pixels[y][x]
    #Obtenemos el color del array con cierta intensidad
    def get_color_with_intensity(self,tx,ty,intensity):
        x= round(tx*self.width)
        y= round(ty*self.height)
        
        r= self.pixels[y][x][0]*intensity
        g= self.pixels[y][x][1]*intensity
        b= self.pixels[y][x][2]*intensity
        
        return color((r/255),(g/255),(b/255))

r=Render(1024,1024)
t=Texture("model.bmp")

r.framebuffer=t.pixels

r.glFinish("t.bmp")