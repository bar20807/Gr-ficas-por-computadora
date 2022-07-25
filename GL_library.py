"""
    gl Library
    
    José Rodrigo Barrera García
    Universidad del Valle de Guatemala
    Carnet: 20807

"""
import struct as st
from collections import namedtuple

V=namedtuple('V',['x','y'])

def char(c):
    # 1 byte
    return st.pack('=c',c.encode('ascii'))

def word(h):
    # 2 bytes
    return st.pack('=h',h)


def dword(d):
    # 4 bytes
    return st.pack('=l',d)

def color(r,g,b):
    return bytes([
        int(b*255), #Se multiplica el número ingresado por 255 para obtener el color
        int(g*255),
        int(r*255)])

#CONSTANTES
BLACK = color(0,0,0)
WHITE = color(1,1,1)

class Render(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.clearColor = BLACK
        self.currColor = WHITE
        self.pixels=[]
        self.glCreateWindow(self.width,self.height)
        self.glViewport(0,0,self.width, self.height)
        self.glClear()
    
    def glCreateWindow(self,width,height):
        self.width=width
        self.height=height
        

    def glViewport(self, posX, posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpWidth = width
        self.vpHeight = height

    def glClearColor(self, r, g, b):
        self.clearColor = color(r,g,b)

    def glColor(self, r, g, b):
        self.currColor = color(r,g,b)

    def glClear(self):
        self.pixels = [[ self.clearColor for y in range(self.height)]
                       for x in range(self.width)]

    def glClearViewport(self, clr = None):
        for x in range(self.vpX, self.vpX + self.vpWidth):
            for y in range(self.vpY, self.vpY + self.vpHeight):
                self.glPoint(x,y,clr)


    def glPoint(self, x, y, clr = None): # Window Coordinates
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currColor

    def glVertex(self, x, y, clr = None): # NDC
        if x > 1 or x < -1 or y > 1 or y < -1:
            print('Fuera del rango del ViewPort')
        else:
            x = (x + 1) * (self.vpWidth/2) + self.vpX
            y = (y + 1) * (self.vpHeight/2) + self.vpY

            x = int(x)
            y = int(y)
            
            self.glPoint(x, y, clr)
                
    
    def glLine(self, v0, v1, clr = None):
        
        # Bresenham line algorithm
        # y = m * x + b
        x0 = v0.x
        x1 = v1.x
        y0 = v0.y
        y1 = v1.y
        
        if x0>1 or x0<-1 or x1>1 or x1<-1 or y0>1 or y0<-1 or y1>1 or y1<-1:
            print('Fuera del rango del ViewPort')
        else:
            #Cálculo del Viewport
            mx0 = int((x0 + 1) * (self.vpWidth/2) + self.vpX)
            my0 = int((y0 + 1) * (self.vpHeight/2) + self.vpY)
            mx1 = int((x1 + 1) * (self.vpWidth/2) + self.vpX)
            my1 = int((y1 + 1) * (self.vpWidth/2) + self.vpY)
            
            
            print("VALORES ANTES DEL FOR mx0: " + str(mx0) + "\nmx1: " + str(mx1))
            print("VALORES ANTES DEL FOR my0: " + str(my0) + "\nmy1: " + str(my1))
            
            dy = abs(my1 - my0)
            dx = abs(mx1 - mx0)

            steep = dy > dx

            # Si la linea tiene pendiente mayor a 1 o menor a -1
            # intercambio las x por las y, y se dibuja la linea
            # de manera vertical
            if steep:
                mx0, my0 = my0, mx0
                mx1, my1 = my1, mx1

            # Si el punto inicial X es mayor que el punto final X,
            # intercambio los puntos para siempre dibujar de 
            # izquierda a derecha       
            if mx0 > mx1:
                mx0, mx1 = mx1, mx0
                my0, my1 = my1, my0

            dy = abs(my1 - my0)
            dx = abs(mx1 - mx0)
            offset = 0
            threshold = dx
            y = my0
        
            for x in range(mx0,mx1):
                offset+=dy*2
                if offset>=threshold:
                    y +=1 if my0 < my1 else -1
                    threshold+=dx*2
                    #print("SOY X DENTRO DE LA CONDICIÓN OFFSET: " + str(x))
                if steep:
                    #print("SOY my0 ANTES DE SER ENVIADA AL VERTEX: " + str(my0))
                    self.glPoint(y,x,clr) 
                else:
                    #print("SOY my0 ANTES DE SER ENVIADA AL VERTEX: " + str(my0))
                    #print("Esta es X ANTES DE SER ENVIADA AL VERTEX: " + str(x) )
                    self.glPoint(x,y,clr)
        
    
    #AREA FINAL DONDE SE ESCRIBE EL ARCHIVO
    def glFinish(self, filename):
        f=open(filename, 'bw')

        #Pixel Header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))
        
        #Info Header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        
        #Pixel Data
        
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.pixels[x][y])
                
        f.close()
     
        
        
        
        
    
    
        