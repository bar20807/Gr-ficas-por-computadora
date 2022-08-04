"""
    gl Library
    
    José Rodrigo Barrera García
    Universidad del Valle de Guatemala
    Carnet: 20807

"""
import struct as st
from collections import namedtuple
from ReadObj import ReadObj
from Vector import Vector3


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
        
            for x in range(mx0,mx1 + 1):
                if steep:
                    #print("SOY my0 ANTES DE SER ENVIADA AL VERTEX: " + str(my0))
                    self.glPoint(y,x,clr) 
                else:
                    #print("SOY my0 ANTES DE SER ENVIADA AL VERTEX: " + str(my0))
                    #print("Esta es X ANTES DE SER ENVIADA AL VERTEX: " + str(x) )
                    self.glPoint(x,y,clr)
                offset+=dy*2
                if offset>=threshold:
                    y +=1 if my0 < my1 else -1
                    threshold+=dx*2
                    #print("SOY X DENTRO DE LA CONDICIÓN OFFSET: " + str(x))
    
    def line(self,v0,v1,clr=None):
        # Bresenham line algorithm
        # y = m * x + b
        x0 = round(v0.x)
        x1 = round(v1.x)
        y0 = round(v0.y)
        y1 = round(v1.y)
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        # Si la linea tiene pendiente mayor a 1 o menor a -1
        # intercambio las x por las y, y se dibuja la linea
        # de manera vertical
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        # Si el punto inicial X es mayor que el punto final X,
        # intercambio los puntos para siempre dibujar de 
        # izquierda a derecha       
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = x1 - x0
        offset = 0
        threshold = dx
        y = y0
        
        for x in range(x0,x1 + 1):
            if steep:
                #print("SOY my0 ANTES DE SER ENVIADA AL VERTEX: " + str(my0))
                self.glPoint(y,x,clr) 
            else:
                #print("SOY my0 ANTES DE SER ENVIADA AL VERTEX: " + str(my0))
                #print("Esta es X ANTES DE SER ENVIADA AL VERTEX: " + str(x) )
                self.glPoint(x,y,clr)
            offset+=dy*2
            if offset>=threshold:
                y +=1 if y0 < y1 else -1
                threshold+=dx*2
                #print("SOY X DENTRO DE LA CONDICIÓN OFFSET: " + str(x))
    
    def transform_vertex(self, Vertex, translate, scale):
        return[
            (Vertex[0]*scale[0]) + translate[0],
            (Vertex[1]*scale[1]) + translate[1]
        ]
        
    def display_obj(self,filename,translate,scale,clr=None):
        dibujo = ReadObj(filename)
        for face in dibujo.faces:
            #Verificamos si es un cuadrado
            if len(face) == 4:
                
                f1=face[0][0]-1
                f2=face[1][0]-1
                f3=face[2][0]-1
                f4=face[3][0]-1

                #Calculamos y mandamos cada uno de los vertices al tranformador de vertices
                v_1 = self.transform_vertex(dibujo.vertices[f1],translate,scale)
                v_2 = self.transform_vertex(dibujo.vertices[f2],translate,scale)
                v_3 = self.transform_vertex(dibujo.vertices[f3],translate,scale)
                v_4 = self.transform_vertex(dibujo.vertices[f4],translate,scale)
                
                #Recorremos los vertices en Line
                self.line(V(v_1[0],v_1[1]),V(v_2[0],v_2[1]),clr)
                self.line(V(v_2[0],v_2[1]),V(v_3[0],v_3[1]),clr)
                self.line(V(v_3[0],v_3[1]),V(v_4[0],v_4[1]),clr)
                self.line(V(v_4[0],v_4[1]),V(v_1[0],v_1[1]),clr)
                
            #Verificamos si las caras son un triangulo
            elif len(face) == 3 :
                f1=face[0][0]-1
                f2=face[1][0]-1
                f3=face[2][0]-1

                #Calculamos y mandamos cada uno de los vertices al tranformador de vertices
                v_1 = self.transform_vertex(dibujo.vertices[f1],translate,scale)
                v_2 = self.transform_vertex(dibujo.vertices[f2],translate,scale)
                v_3 = self.transform_vertex(dibujo.vertices[f3],translate,scale)
                
                #Recorremos los vertices en Line
                self.line(V(v_1[0],v_1[1]),V(v_2[0],v_2[1]),clr)
                self.line(V(v_2[0],v_2[1]),V(v_3[0],v_3[1]),clr)
                self.line(V(v_3[0],v_3[1]),V(v_1[0],v_1[1]),clr)
                
                
            
                
    # Función que revisa si hay algún punto en un poligono
    def pointInside(self, x, y, poligono):
        isInside = False
        n = len(poligono)
        x0, y0 = poligono[0]
        for j in range(n+1):
            x2, y2 = poligono[j % n]
            if y > min(y0, y2):
                if y <= max(y0, y2):
                    if x <= max(x0, x2):
                        if y0 is not y2:
                            inX = (y-y0)*(x2-x0)/(y2-y0)+x0
                        if x0 == x2 or x <= inX:
                            isInside = not isInside
            x0, y0 = x2, y2
        return isInside
    # Función que llena un poligono
    def scanFillpoly(self, poligono, clr=None):
        for x in range(self.width):
            for y in range(self.height):
                if self.pointInside(x, y, poligono):
                    self.glPoint(x, y, clr) or color(1, 0, 0)

    # Función que dibuja un poligono
    def drawPolygon(self, polygon, clr=None):
        for i in range(100):
            for idx, (x, y) in enumerate(polygon):
                polygon[idx] = V(x, y)

        for i in range(len(polygon)):
            self.line(polygon[i], polygon[(i - 1) %
                        len(polygon)], clr)    
        
    
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
     
        
        
        
        
    
    
        