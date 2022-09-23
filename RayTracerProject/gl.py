"""
    gl Library
    
    José Rodrigo Barrera García
    Universidad del Valle de Guatemala
    Carnet: 20807

"""
import struct as st
from ReadObj import ReadObj
from Vector import *



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
    
    def glCreateWindow(self,width, height):
            if width % 4 == 0 and height % 4 == 0:
                self.width = width 
                self.height = height 

            elif width < 0 or height < 0:
                print("Error")
            else: 
                print("Error")
        

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
        self.zBuffer = [[ -99999 for x in range(self.width)]
                       for y in range(self.height)]

    def glClearViewport(self, clr = None):
        for x in range(self.vpX, self.vpX + self.vpWidth):
            for y in range(self.vpY, self.vpY + self.vpHeight):
                self.glPoint(x,y,clr)


    def glPoint(self, x, y, clr = None): # Window Coordinates
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.framebuffer[y][x] = clr or self.currColor

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
        #print("ESTA ES LA ESCALA: ", scale)
        return V3(
            round((Vertex[0]*scale[0]) + translate[0]),
            round((Vertex[1]*scale[1]) + translate[1]),
            round((Vertex[2]*scale[2]) + translate[2])
        )
        
    def display_obj(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), texture=None):
        dibujo = ReadObj(filename)
        #Hacemos una fuente de luz
        L=V3(0,0,1)
        for face in dibujo.faces:
            vcount = len(face)

            if vcount == 3:
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1

                a = self.transform_vertex(dibujo.vertices[f1], translate, scale)
                b = self.transform_vertex(dibujo.vertices[f2], translate, scale)
                c = self.transform_vertex(dibujo.vertices[f3], translate, scale)
                
                
                #Calculamos la normal para todo el triangulo
                N=(b-a)*(c-a)
                
                #print("Hola: ", N.x, N.y, N.z)
                #print("Hola: ", L.x, L.y, L.z)
                
                #Calculamos la intensidad que hay entre la normal y la luz
                i= (N.norm() @ L.norm())
                
                if i < 0: 
                    i = abs(i) 
                    #print(i)
                if i > 1:
                    i = 1
                
                if not texture:
                    grey = round(255 * i)
                    if grey < 0:
                        continue
                    self.triangle(a, b, c, color=color(grey/255, grey/255, grey/255))
                else:
                    t1 = face[0][1] - 1
                    t2 = face[1][1] - 1
                    t3 = face[2][1] - 1
                    tA = V3(*dibujo.tvertices[t1])
                    tB = V3(*dibujo.tvertices[t2])
                    tC = V3(*dibujo.tvertices[t3])

                    self.triangle(a, b, c, texture=texture, texCoords=(tA, tB, tC), intensity=i)
            else:
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1
                f4 = face[3][0] - 1   

                vertices = [
                    self.transform_vertex(dibujo.vertices[f1], translate, scale),
                    self.transform_vertex(dibujo.vertices[f2], translate, scale),
                    self.transform_vertex(dibujo.vertices[f3], translate, scale),
                    self.transform_vertex(dibujo.vertices[f4], translate, scale)
                ]
                
                #Calculamos la normal para todo el triangulo
                N=(vertices[0]-vertices[1])*(vertices[1]-vertices[2])
                
                #print("Hola: ", N.x, N.y, N.z)
                #print("Hola: ", L.x, L.y, L.z)
                
                #Calculamos la intensidad que hay entre la normal y la luz
                i= (N.norm() @ L.norm())
                
                if i < 0: 
                    i = abs(i) 
                    #print(i)
                if i > 1:
                    i = 1

                grey = round(255 * i)

                A, B, C, D = vertices 

                if not texture:
                    grey = round(255 * i)
                    if grey < 0:
                        continue
                    self.triangle(A, B, C, color(grey/255, grey/255, grey/255))
                    self.triangle(A, C, D, color(grey/255, grey/255, grey/255))            
                else:
                    t1 = face[0][1] - 1
                    t2 = face[1][1] - 1
                    t3 = face[2][1] - 1
                    t4 = face[3][1] - 1
                    tA = V3(*dibujo.tvertices[t1])
                    tB = V3(*dibujo.tvertices[t2])
                    tC = V3(*dibujo.tvertices[t3])
                    tD = V3(*dibujo.tvertices[t4])
                    
                    self.triangle(A, B, C, texture=texture, texCoords=(tA, tB, tC), intensity=i)
                    self.triangle(A, C, D, texture=texture, texCoords=(tA, tC, tD), intensity=i)
                
          
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
            
        
    
    def triangle(self, A, B, C, texCoords = (), texture = None, color = None, intensity = 1):
        
        bbox_min, bbox_max = bounding_box(A, B, C)

        for x in range(bbox_min.x, bbox_max.x + 1):
            for y in range(bbox_min.y, bbox_max.y + 1):
                w, v, u = barycentric(A, B, C, V3(x, y))
                if w < 0 or v < 0 or u < 0:
                    continue
                
                if texture:
                    tA, tB, tC = texCoords
                    tx = tA.x * w + tB.x * v + tC.x * u
                    ty = tA.y * w + tB.y * v + tC.y * u
                    
                    color = texture.get_color(tx, ty, intensity)

                z = A.z * w + B.z * v + C.z * u

                if x < 0 or y < 0:
                    continue

                if x < len(self.zBuffer) and y < len(self.zBuffer[x]) and z > self.zBuffer[x][y]:
                    self.glPoint(x, y, color)
                    self.zBuffer[x][y] = z

                
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