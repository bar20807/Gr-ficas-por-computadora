"""
    gl Library
    
    José Rodrigo Barrera García
    Universidad del Valle de Guatemala
    Carnet: 20807

"""
import struct as st

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
        self.width=width
        self.height=height
        self.glclearColor = WHITE
        self.currentcolor=BLACK
        self.glClear()
        self.glViewPort(int(self.width/4),int(self.height/4),int(self.width/2),int(self.height/2))
        self.glCreateWindow(self.width,self.height)
        self.framebuffer=[]
           
    def glCreateWindow(self,width,height):
        self.width=width
        self.height=height
        self.glClear()
    
    def glViewPort(self,x,y,width,height):
        self.vpx=x
        self.vpy=y
        self.vpwidth=width
        self.vpheight=height
    
    """
        EJEMPLO SACADO DE:
        https://stackoverflow.com/questions/15693231/normalized-device-coordinates
        
        s_x * X_NDC + d_x = X_pixel
        s_y * Y_NDC + d_y = Y_pixel
        
        s_x = ( N_x - epsilon ) / 2
        d_x = ( N_x - epsilon ) / 2

        s_y = ( N_y - epsilon ) / (-2*a)
        d_y = ( N_y - epsilon ) / 2

        epsilon = .001
        a = N_y/N_x  (physical screen aspect ratio)
            
    """
    """
        ÁREA DE DIBUJO DE CADA UNA DE LAS VENTANAS, VIEWPORT, WINDOW Y EL PUNTO FINAL
    
    """
    def glclearViewPort(self,Color=None):
        for i in range(self.vpx, self.vpx + self.vpwidth):
            for j in range(self.vpy, self.vpy + self.vpheight):
                self.point(i, j, Color)
        
    
    def glVertex(self, x, y, Color=None):
        if x > 0.9999 or x < -0.9999 or y > 0.9999 or y < -0.9999:
            print('Fuera del rango del ViewPort')
        else:
            x = (x + 1) * (self.vpwidth/2) + self.vpx
            y = (y + 1) * (self.vpheight/2) + self.vpy

            x = int(x)
            y = int(y)
            
            self.point(x, y, Color)
    
    #FUNCIONES PARA AGREGAR EL COLOR DE FONDO
    
    def color(self,r,g,b):
        self.currentcolor=color(r,g,b)
        
    def glClear(self):
        self.framebuffer = [
            [self.glclearColor for x in range (self.width)]
            for y in range (self.height)
                            ]
    #Agregar fondo a la ventana que se está creando
    def glClearColor(self,r,g,b):
        self.glclearColor = color(r,g,b)
    
    def point(self,x,y,Color=None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.framebuffer[x][y] = Color or self.currentcolor
    
    #Función para realizar una línea
    def glLine(self, x0,y0, x1,y1, color = None):
           
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        threshold = dx

        y = int(y0)
        for x in range(int(x0), int(x1 + 1)):
            if steep:
                self.point(y, x, color)
            else:
                self.point(x, y, color)
            
            offset += dy * 2
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += dx * 2
        
    
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
                f.write(self.framebuffer[x][y])
                
        f.close()
     
        
        
        
        
    
    
        