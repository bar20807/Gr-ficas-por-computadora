from ast import Pass

from sympy import false, true
from GL_library import Render, color

def SR1(x,y,r,g,b):

    #INSTANCIAS DE MI RENDER

    MyRender = Render(1000,1000)
    MyRender.glClearColor(0.49, 0.49, 0.49)
    MyRender.glClear()
    MyRender.glclearViewPort(color(0, 0, 0))
    MyRender.glVertex(x, y, color(r, g, b))
    MyRender.glFinish('b.bmp')

def SR2():
    pass
    

iterador= false
opciones= 0

while not iterador:
    
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+ BIENVENIDO A MI RENDER -+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("\n 1) Mostrar SR1: \n 2) Mostrar SR2" "\n 3) Salir: ")
    opciones= int(input("\n Elige una de las siguientes opciones: "))
    
    
    try:
        if opciones == 1:
            x = float(input("Porfavor, ingrese una coordenada en X con rango de (0 a 1): "))
            y = float(input("Porfavor, ingrese una coordenada en Y con rango de (0 a 1): "))
            r= float(input("Porfavor, ingrese el color r con rango de (0 a 1): "))
            g= float(input("Porfavor, ingrese el color g con rango de (0 a 1): "))
            b= float(input("Porfavor, ingrese el color b con rango de (0 a 1): "))
            
            if 0<x<1 & 0<y<1 & 0<r<1 & 0<g<1 & 0<b<1:
                print("Usted no ingresó un valor válido en rango indicado")
            else:
                SR1(x,y,r,g,b)
                
        elif opciones == 2:
            iterador = true
        elif opciones == 3:
            iterador = true
            print("Gracias por usar mi render.")
            
    except:
        print("Usted ingresó un carecter no válido... Intente de nuevo")

