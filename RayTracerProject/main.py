from RayTracer import *


def drawing_a_snowman():
    r = RayTracer(2024,2024)
    r.scene = [
    (Sphere(V3(2.8, 0, -16), 0.3), color(1,0,0)), #Nariz
    (Sphere(V3(3.3, 1, -16), 0.3), color(0,0,0)), #Ojo
    (Sphere(V3(3.3, -1, -16), 0.3), color(0,0,0)), #Ojo
    (Sphere(V3(2.6, 1, -16), 0.2), color(0,0,0)), #Boca
    (Sphere(V3(2.6, -1, -16), 0.2), color(0,0,0)), #Boca
    (Sphere(V3(2.4, 0.5, -16), 0.2), color(0,0,0)), #Boca
    (Sphere(V3(2.4, -0.5, -16), 0.2), color(0,0,0)), #Boca
    (Sphere(V3(2.2, 0, -16), 0.2), color(0,0,0)), #Boca
    (Sphere(V3(-0.8, 0, -16), 0.3), color(0,0,0)), #Botón 
    (Sphere(V3(0.1, 0, -16), 0.3), color(0,0,0)), #Botón
    (Sphere(V3(1, 0, -16), 0.3), color(0,0,0)), #Botón
    (Sphere(V3(-4, 0, -16), 3), color(1,1,1)), #Esfera del cuerpo
    (Sphere(V3(0, 0, -16), 2.1), color(1,1,1)), #Esfera del cuerpo
    (Sphere(V3(3, 0, -16), 1.5), color(1,1,1)),] #Esfera del cuerpo
    r.render()
    r.write('RT1.bmp')

iterador= False
opciones= 0

while not iterador:
    
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+ BIENVENIDO A MI Raytracer -+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("\n 1) Mostrar RT1 \n 2) ..." "\n 3) ... \n 4) ... \n 5) ... \n 6) Salir")
    opciones= int(input("\n Elige una de las siguientes opciones: "))
    
    
    try:
        if opciones == 1:
            drawing_a_snowman()
        elif opciones == 2:
            
            iterador= True
            
        elif opciones == 3:
            iterador= True
        
        elif opciones==4:
            iterador= True
        
        elif opciones==5:
            iterador= True
        elif opciones==6:
            iterador=True
            print("Gracias por usar mi raytracer")
            
            
            
    except Exception as e:
        print( e + "\nUsted ingresó un carecter no válido... Intente de nuevo")