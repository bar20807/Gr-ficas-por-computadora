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
def drawing_a_bears():

    r = RayTracer(2024, 2024)
    r.light = Light(V3(-4, -4, 0), 1, Color(255,255,255))

    r.scene = [
        Sphere(V3(-3, -1.65, -14), 1.65, Material(diffuse=Color(135, 70, 20))), #Cabeza
        Sphere(V3(3, -1.65, -14), 1.65, Material(diffuse=Color(135, 70, 20))), #Cabeza
        Sphere(V3(-4.6, 0.7, -12.2), 1, Material(diffuse=Color(135, 70, 20))), #Mano
        Sphere(V3(-1, 0.7, -13), 1, Material(diffuse=Color(135, 70, 20))), #Mano
        Sphere(V3(-3.7, -3, -12.7), 0.7, Material(diffuse=Color(135, 70, 20))), #Oreja
        Sphere(V3(-2, -3, -13), 0.7, Material(diffuse=Color(135, 70, 20))), #Oreja
        Sphere(V3(-2.5, -1.5, -10), 0.2, Material(diffuse=Color(0, 0, 0))), #Nariz punto
        Sphere(V3(-1.8, -1.5, -10), 0.2, Material(diffuse=Color(0, 0, 0))), #Ojo
        Sphere(V3(2.5, -1.5, -10), 0.2, Material(diffuse=Color(0, 0, 0))), #Ojo
        Sphere(V3(1.8, -1.5, -10), 0.2, Material(diffuse=Color(0, 0, 0))) , #Ojo
        Sphere(V3(-2.2, -0.78, -10), 0.2, Material(diffuse=Color(0, 0, 0))), #Ojo
        Sphere(V3(2.2, -0.78, -10), 0.2, Material(diffuse=Color(0, 0, 0))),  #Nariz punto
        Sphere(V3(-3.6, 3.3, -12.1), 1, Material(diffuse=Color(135, 70, 20))), #Pie
        Sphere(V3(-1.7, 3.3, -12.4), 1, Material(diffuse=Color(135, 70, 20))), #Pie
        Sphere(V3(4.2, 0.7, -12.2), 1, Material(diffuse=Color(135, 70, 20))), #Mano
        Sphere(V3(1, 0.7, -12.6), 1, Material(diffuse=Color(135, 70, 20))), #Mano
        Sphere(V3(3.6, -3, -12.7), 0.7, Material(diffuse=Color(135, 70, 20))), #Oreja
        Sphere(V3(2, -3, -13), 0.7, Material(diffuse=Color(135, 70, 20))), #Oreja
        Sphere(V3(1.6, 3.15, -12.1), 0.95, Material(diffuse=Color(135, 70, 20))), #Pie
        Sphere(V3(3.6, 3.1, -12), 0.95, Material(diffuse=Color(135, 70, 20))), #Pie
        Sphere(V3(-2.8, -0.82, -13), 0.8, Material(diffuse=Color(199, 144, 90))), #Nariz
        Sphere(V3(2.8, -0.82, -13), 0.8, Material(diffuse=Color(199, 144, 90))), #Nariz
        Sphere(V3(-3, 2, -14), 2.35, Material(diffuse=Color(135, 70, 20))), #Cuerpo
        Sphere(V3(3, 2, -14), 2.35, Material(diffuse=Color(135, 70, 20))), #Cuerpo
    ]
    r.point(100, 100)
    r.render()
    r.write('RT2.bmp')

def Proyecto2():
    return ""
    
    
iterador= False
opciones= 0

while not iterador:
    
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+ BIENVENIDO A MI Raytracer -+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("\n 1) Mostrar RT1 \n 2) Mostrar RT2 " "\n 3) Proyecto (Proximamente...) \n 4) Salir ")
    opciones= int(input("\n Elige una de las siguientes opciones: "))
    
    
    try:
        if opciones == 1:
            drawing_a_snowman()
        elif opciones == 2:
            drawing_a_bears()          
        elif opciones == 3:
            Proyecto2() 
        elif opciones==4:
            iterador= True
            print("Gracias por usar mi raytracer")
            
            
            
    except Exception as e:
        print( e + "\nUsted ingresó un carecter no válido... Intente de nuevo")