from ast import Pass

from sympy import false, true
from GL_library import Render, color,V

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
    
    V0=V(x0,y0)
    V1=V(x1,y1)
    
    #INSTANCIAS DE MI RENDER LÍNEA
    MyRender = Render(500,500)
    MyRender.glViewport(int(500/4), int(500/4), int(500/2), int(500/2))
    MyRender.glClearColor(0.5, 0.5, 0.5)
    MyRender.glClear()
    MyRender.glClearViewport(color(0, 0, 0))
    MyRender.glLine(V0,V1,color(1,0,0))
    MyRender.glFinish('line.bmp')

iterador= false
opciones= 0

while not iterador:
    
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+ BIENVENIDO A MI RENDER -+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("\n 1) Mostrar SR1 \n 2) Mostrar SR2" "\n 3) Salir ")
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
            iterador = true
            print("Gracias por usar mi render.")
            
    except Exception as e:
        print( e + "\nUsted ingresó un carecter no válido... Intente de nuevo")


