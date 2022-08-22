"""
    gl Library
    
    José Rodrigo Barrera García
    Universidad del Valle de Guatemala
    Carnet: 20807

"""
from cgi import print_environ
from re import U
import struct as st
from collections import namedtuple
from tkinter import W
from ReadObj import ReadObj
from Vector import *
from texture import *

V=namedtuple('V',['x','y'])
texture=Texture()

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

#Función para realizar tríangulos
def bounding_box(A,B,C):
    vers = [(A.x,A.y),(B.x,B.y),(C.x,C.y)]
    
    xmin=999999
    xmax=-999999
    ymin=999999
    ymax=-999999
    
    for (x,y) in vers:
        if x<xmin:
            xmin=x
        if x>xmax:
            xmax=x
        if y<ymin:
            ymin=y
        if y>ymax:
            ymax=y
    
    return V3(xmin,ymin),V3(xmax,ymax)

def cross(v0,v1):
    return (
            v0.y*v1.z-v0.z*v1.y,
            v0.z*v1.x-v0.x*v1.z,
            v0.x*v1.y-v0.y*v1.x
    )
    

def barycentric(A,B,C,P):
    cx,cy,cz=cross(
        V3(B.x-A.x,C.x-A.x,A.x-P.x),
        V3(B.y-A.y,C.y-A.y,A.y-P.y)
    )
    
    if abs(cz) < 1:
        return -1, -1, -1
    
    u = cx/cz
    v = cy/cz
    w = 1 - (u + v)

    return (w, v, u)

#CONSTANTES
BLACK = color(0,0,0)
WHITE = color(1,1,1)

class Render(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.clearColor = BLACK
        self.currColor = WHITE
        self.framebuffer=[]
        self.zBuffer=[]
        self.texture=None
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
        self.framebuffer = [[ self.clearColor for x in range(self.width)]
                       for y in range(self.height)]
        self.zBuffer = [[ -9999 for x in range(self.width)]
                       for y in range(self.height)]

    def glClearViewport(self, clr = None):
        for x in range(self.vpX, self.vpX + self.vpWidth):
            for y in range(self.vpY, self.vpY + self.vpHeight):
                self.glPoint(x,y,clr)


    def glPoint(self, x, y, clr = None): # Window Coordinates
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.framebuffer[x][y] = clr or self.currColor

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
        return V3(
            round((Vertex[0]*scale[0]) + translate[0]),
            round((Vertex[1]*scale[1]) + translate[1]),
            round((Vertex[2]*scale[2]) + translate[2])
        )
        
    def display_obj(self,filename,filename2,translate,scale,clr=None):
        dibujo = ReadObj(filename)
        texture.read(filename2)
        if filename2: 
            texture.read(filename2)
            self.texture=filename2
        for face in dibujo.faces:
            #Verificamos si es un cuadrado
            if len(face) == 4:
                if self.texture:
                    
                    f1=face[0][0]-1
                    f2=face[1][0]-1
                    f3=face[2][0]-1
                    f4=face[3][0]-1

                    #Calculamos y mandamos cada uno de los vertices al tranformador de vertices
                    v_1 = self.transform_vertex(dibujo.vertices[f1],translate,scale)
                    v_2 = self.transform_vertex(dibujo.vertices[f2],translate,scale)
                    v_3 = self.transform_vertex(dibujo.vertices[f3],translate,scale)
                    v_4 = self.transform_vertex(dibujo.vertices[f4],translate,scale)
                    
                    print("Entre a texturas")
                
                    #Cargamos las caras de las texturas
                    ft1=face[0][1]-1
                    ft2=face[1][1]-1
                    ft3=face[2][1]-1
                    ft4=face[3][1]-1

                    #Calculamos y mandamos cada uno de los vertices de texturas
                    vt_1 = V3(*dibujo.tvertices[ft1])
                    vt_2 = V3(*dibujo.tvertices[ft2])
                    vt_3 = V3(*dibujo.tvertices[ft3])
                    vt_4 = V3(*dibujo.tvertices[ft4])
                    
                    #Recorremos los vertices en Triangle                
                    self.triangle(
                        (v_1,v_2,v_4),
                        (vt_1,vt_2,vt_4))
                    self.triangle(
                        (v_2,v_3,v_4),
                        (vt_2,vt_3,vt_4))
                else:
                    
                    f1=face[0][0]-1
                    f2=face[1][0]-1
                    f3=face[2][0]-1
                    f4=face[3][0]-1

                    #Calculamos y mandamos cada uno de los vertices al tranformador de vertices
                    v_1 = self.transform_vertex(dibujo.vertices[f1],translate,scale)
                    v_2 = self.transform_vertex(dibujo.vertices[f2],translate,scale)
                    v_3 = self.transform_vertex(dibujo.vertices[f3],translate,scale)
                    v_4 = self.transform_vertex(dibujo.vertices[f4],translate,scale)
                          
                    #print("VALORES DE V_1: ",v_1)

                    #Recorremos los vertices en Line
                    self.triangle((v_1,v_2,v_4))
                    self.triangle((v_2,v_3,v_4))
                
            #Verificamos si las caras son un triangulo
            if len(face) == 3 :
                if self.texture:
                    
                    f1=face[0][0]-1
                    f2=face[1][0]-1
                    f3=face[2][0]-1

                    #Calculamos y mandamos cada uno de los vertices al tranformador de vertices
                    v_1 = self.transform_vertex(dibujo.vertices[f1],translate,scale)
                    v_2 = self.transform_vertex(dibujo.vertices[f2],translate,scale)
                    v_3 = self.transform_vertex(dibujo.vertices[f3],translate,scale)
                    
                    print("Entre a texturas")
                
                    #Cargamos las caras de las texturas
                    ft1=face[0][1]-1
                    ft2=face[1][1]-1
                    ft3=face[2][1]-1

                    #Calculamos y mandamos cada uno de los vertices de texturas
                    vt_1 = V3(*dibujo.tvertices[ft1])
                    vt_2 = V3(*dibujo.tvertices[ft2])
                    vt_3 = V3(*dibujo.tvertices[ft3])
                    
                    #Recorremos los vertices en Triangle                
                    self.triangle(
                        (v_1,v_2,v_3),
                        (vt_1,vt_2,vt_3))
                else:
                    f1=face[0][0]-1
                    f2=face[1][0]-1
                    f3=face[2][0]-1

                    #Calculamos y mandamos cada uno de los vertices al tranformador de vertices
                    v_1 = self.transform_vertex(dibujo.vertices[f1],translate,scale)
                    v_2 = self.transform_vertex(dibujo.vertices[f2],translate,scale)
                    v_3 = self.transform_vertex(dibujo.vertices[f3],translate,scale)
                    self.triangle((v_1,v_2,v_3))
                
                
                
            
                
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
                polygon[idx] = V(x,y)

        for i in range(len(polygon)):
            self.line(polygon[i], polygon[(i - 1) %
                        len(polygon)], clr)    
    
    def triangle_std(self,A,B,C,clr=None):
        if A.y > B.y:
            A,B=B,A
        if A.y>C.y:
            A,C=C,A
        if B.y > C.y:
            B,C=C,B
        
        dx_ac= C.x-A.x
        dy_ac= C.y-A.y
        
        if dy_ac==0:
            return
        
        mi_ac=dx_ac/dy_ac

        dx_ab=B.x-A.x
        dy_ab=B.y-A.y
        
        if dy_ab!=0:
            mi_ab=dx_ab/dy_ab
            for y in range(round(A.y),round(B.y+1)):
                xi= round(A.x - mi_ac*(A.y-y))
                xf= round(A.x - mi_ab*(A.y-y))
                if xi>xf:
                    xi,xf=xf,xi
                    
                for x in range(xi,xf):
                    self.glPoint(x,y,clr)
        
        dx_bc=C.x-B.x
        dy_bc=C.y-B.y
        
        if dy_bc!=0:
            mi_bc=dx_bc/dy_bc  
            for y in range(round(B.y),round(C.y+1)):
                xi= round(A.x - mi_ac*(A.y-y))
                xf= round(B.x - mi_bc*(B.y-y))
                if xi>xf:
                    xi,xf=xf,xi
                    
                for x in range(xi,xf):
                    self.glPoint(x,y,clr)
            
        
    
    def triangle(self,vertices,tvertices=(),clr=None):
        
        A,B,C=vertices
        print("ESTO ES TVERTICES",tvertices)
        if self.texture:
            tA,tB,tC=tvertices
        
        #Hacemos una fuente de luz
        L=V3(0,0,-1)
        
        #Calculamos la normal para todo el triangulo
        N=(C-A)*(B-A)
        
        #print("Hola: ", N.x, N.y, N.z)
        #print("Hola: ", L.x, L.y, L.z)
        
        #Calculamos la intensidad que hay entre la normal y la luz
        
        i= (N.norm() @ L.norm())
        #print(i)
        
        #print(N.norm() @ L.norm())
        
        #print("ESTE ES EL VALOR DE I: ",i)

        #i = 1/i
        
        #print("i invertida", i)
        
        #print("Intensidad: ", i)
        
        if i < 0: 
            i = abs(i) 
        #print(i).
        if i > 1:
            i = 1
            
        grey= 1*i
        
        #print("ESTE ES EL COLOR QUE SE ENVÍA: ", grey)
        
        self.currColor=color(
            grey,
            grey,
            grey
        )
        
        Bmin,Bmax = bounding_box(A,B,C)
        
        Bmin.round()
        Bmax.round()
        
        for x in range(Bmin.x,Bmax.x+1):
            for y in range(Bmin.y,Bmax.y+1):
                w,v,u= barycentric(A,B,C,V3(x,y))
                if (w<0 or v<0 or u<0):
                    continue
                #Calculamos Z
                z=A.z*w + B.z*v + C.z*u
                if (self.zBuffer[x][y] < z):
                    self.zBuffer[x][y]=z
                    if self.texture:
                        tx= tA.x*w + tB.x*u+tC.x*v
                        print("VALORES DE tx: ",tx)
                        ty= tA.y*w + tB.y*u+tC.y*v
                        self.currColor= texture.get_color_with_intensity(tx,ty,i)
                    self.glPoint(y,x)
    
    def triangle_texture(self,filename,filename2,clr):
        dibujo = ReadObj(filename)
        texture.read(filename2)
        self.framebuffer=texture.pixels  
        #Verificamos si las caras son un triangulo
        for face in dibujo.faces:
            if len(face) == 3:
                f1=face[0][0]-1
                f2=face[1][0]-1
                f3=face[2][0]-1
                        
                print("Entre a texturas")
                    
                #Calculamos y mandamos cada uno de los vertices de texturas
                vt_1 = V3(
                    dibujo.tvertices[f1][0]*texture.width,
                    dibujo.tvertices[f1][1]*texture.height
                    )
                vt_2 = V3(
                    dibujo.tvertices[f2][0]*texture.width,
                    dibujo.tvertices[f2][1]*texture.height
                    )
                vt_3 = V3(
                    dibujo.tvertices[f3][0]*texture.width,
                    dibujo.tvertices[f3][1]*texture.height
                    )
                #Recorremos las texturas con glLine              
                self.line(vt_1,vt_2,clr)
                self.line(vt_2,vt_3,clr)
                self.line(vt_3,vt_1,clr)
                
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
        
        for y in range(self.height):
            for x in range(self.width):
                f.write(self.framebuffer[y][x])
                
        f.close()
        
        
        
    
    
        