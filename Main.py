from GL_library import Render, color
from Vector import *
from texture import Texture
from math import *


# 13,20,80,40

def SR1(x,y,r,g,b):

    #INSTANCIAS DE MI RENDER

    MyRender = Render(500,500)
    MyRender.glViewport(int(500/4), int(500/4), int(500/2), int(500/2))
    MyRender.glClearColor(0.5, 0.5, 0.5)
    MyRender.glClear()
    MyRender.glClearViewport(color(0, 0, 0))
    MyRender.glVertex(x,y,color(r,g,b))
    MyRender.glFinish('b.bmp')

def SR2(x0,y0,x1,y1):
    
    V0=V3(x0,y0)
    V1=V3(x1,y1)
    
    #INSTANCIAS DE MI RENDER LÍNEA
    MyRender = Render(500,500)
    MyRender.glViewport(0, 0, 500, 500)
    MyRender.glClearColor(0.5, 0.5, 0.5)
    MyRender.glClear()
    MyRender.glClearViewport(color(0, 0, 0))
    MyRender.glLine(V0,V1,color(1,0,0))
    MyRender.glFinish('line.bmp')

def DrawHouse():
     
    #VECTORES PARA DIBUJAR LA CASA
    #V0=V(0.3,-0.5)
    #V1=V(0.3,-0.1)
    
    #INSTANCIAS
    MyRender = Render(500,500)
    MyRender.glViewport(0,0,500,500)
    MyRender.glClearColor(0.5,0.5,0.5)
    MyRender.glClear()
    MyRender.glClearViewport(color(0,0,0))
    
    #PRIMERA PARED
    MyRender.glLine(V3(0.2,-0.4),V3(0.2,-0.05),color(1,0,0)) #LÍNEA 1 DEL CUADRADO
    MyRender.glLine(V3(0.6,-0.4),V3(0.6,-0.05),color(1,0,0)) #LÍNEA 2 BAJA DEL CUADRADO
    MyRender.glLine(V3(0.2,-0.4),V3(0.6,-0.4),color(1,0,0))  #LÍNEA 3 IZQUIERDA DEL CUADRADO
    MyRender.glLine(V3(0.2,-0.05),V3(0.6,-0.05),color(1,0,0)) #LÍNEA 4 DERECHA DEL CUADRADO
    
    #TECHO DE LA PARED
    MyRender.glLine(V3(0.6,-0.4),V3(0.8,-0.2),color(1,1,0))
    MyRender.glLine(V3(0.6,-0.05),V3(0.8,-0.2),color(0,1,0))
    
    #SEGUNDA PARED (FRONTAL)    
    MyRender.glFinish('house.bmp')

def DrawPolligons():
    MyRender = Render(1000,1000)
    MyRender.glViewport(0,0,1000,1000)
    MyRender.glClearColor(0.5,0.5,0.5)
    MyRender.glClear()
    MyRender.glClearViewport(color(0,0,0))
    
    star = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330),
        (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

    square = [(321, 335), (288, 286), (339, 251), (374, 302)]

    triangle = [(377, 249), (411, 197), (436, 249)]

    pol4 = [(413, 177), (448, 159), (502, 88),
            (553, 53), (535, 36), (676, 37), (660, 52),
            (750, 145), (761, 179), (672, 192), (659, 214),
            (615, 214), (632, 230), (580, 230),
            (597, 215), (552, 214), (517, 144), (466, 180)]

    pol5 = [(682, 175), (708, 120), (735, 148), (739, 170)]

    MyRender.drawPolygon(star, color(1,1,1))
    MyRender.scanFillpoly(star, color(1,0,0))
    MyRender.drawPolygon(square, color(0.99,0.99,0.6))
    MyRender.scanFillpoly(square, color(0.99,0.99,0.6))
    MyRender.drawPolygon(triangle, color(0,0.6,0))
    MyRender.scanFillpoly(triangle, color(0,0.6,0))
    MyRender.drawPolygon(pol4, color(1,1,1))
    MyRender.scanFillpoly(pol4, color(1,1,1))
    MyRender.drawPolygon(pol5, color(1,0,0))
    MyRender.scanFillpoly(pol5, color(1,0,0))
    
    MyRender.glFinish("Poligonos.bmp")
    

def Read_Objects():
    MyRender = Render(1000, 1000)
    t=Texture('model.bmp')
    MyRender.lookAt(V3(0,0,1), V3(0,0,0), V3(0,1,0))
    MyRender.display_obj('model.obj', (512, 500, 0), (400, 400, 500),(0,pi/8,0), texture=t)
    MyRender.glFinish('MatrixPrueba.bmp')
    

iterador= False
opciones= 0

while not iterador:
    
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+ BIENVENIDO A MI RENDER -+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("\n 1) Mostrar SR1 \n 2) Mostrar SR2" "\n 3) Dibujar una casa utilizando glLine \n 4) Dibujar poligonos \n 5) Renderizar un modelo \n 6) Salir")
    opciones= int(input("\n Elige una de las siguientes opciones: "))
    
    
    try:
        if opciones == 1:
            x = float(input("Porfavor, ingrese una coordenada en X con rango de (0 a 1): "))
            y = float(input("Porfavor, ingrese una coordenada en Y con rango de (0 a 1): "))
            r= float(input("Porfavor, ingrese el color r con rango de (0 a 1): "))
            g= float(input("Porfavor, ingrese el color g con rango de (0 a 1): "))
            b= float(input("Porfavor, ingrese el color b con rango de (0 a 1): "))
            
            if 0<r<1 & 0<g<1 & 0<b<1:
                print("Usted no ingresó un valor válido en rango indicado")
            else:
                SR1(x,y,r,g,b)
                
        elif opciones == 2:
            
            x0=float(input("Porfavor, ingrese su coordenada inicial (x0): "))
            y0=float(input("Porfavor, ingrese su coordenada inicial (y0): "))
            x1=float(input("Porfavor, ingrese su coordenada inicial (x1): "))
            y1=float(input("Porfavor, ingrese su coordenada inicial (y1): "))
            
            SR2(x0,y0,x1,y1)
            
        elif opciones == 3:
            DrawHouse()
        
        elif opciones==4:
            DrawPolligons()
        
        elif opciones==5:
            Read_Objects()
        elif opciones==6:
            iterador=True
            print("Gracias por usar mi renderer")
            
            
            
    except Exception as e:
        print( e + "\nUsted ingresó un carecter no válido... Intente de nuevo")


