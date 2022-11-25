from RayTracer import *
from AmbientLight import *

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
        Sphere(V3(-3, -1.65, -14), 1.65, Material(diffuse=Color(135, 70, 20), albedo=[0.8, 0.2], spec=30)), #Cabeza
        Sphere(V3(3, -1.65, -14), 1.65, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Cabeza
        Sphere(V3(-4.6, 0.7, -12.2), 1, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Mano
        Sphere(V3(-1, 0.7, -13), 1, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Mano
        Sphere(V3(-3.7, -3, -12.7), 0.7, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Oreja
        Sphere(V3(-2, -3, -13), 0.7, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Oreja
        Sphere(V3(-2.5, -1.5, -10), 0.2, Material(diffuse=Color(0, 0, 0),albedo=[0.8, 0.2], spec=30)), #Nariz punto
        Sphere(V3(-1.8, -1.5, -10), 0.2, Material(diffuse=Color(0, 0, 0),albedo=[0.8, 0.2], spec=30)), #Ojo
        Sphere(V3(2.5, -1.5, -10), 0.2, Material(diffuse=Color(0, 0, 0),albedo=[0.8, 0.2], spec=30)), #Ojo
        Sphere(V3(1.8, -1.5, -10), 0.2, Material(diffuse=Color(0, 0, 0),albedo=[0.8, 0.2], spec=30)) , #Ojo
        Sphere(V3(-2.2, -0.78, -10), 0.2, Material(diffuse=Color(0, 0, 0),albedo=[0.8, 0.2], spec=30)), #Ojo
        Sphere(V3(2.2, -0.78, -10), 0.2, Material(diffuse=Color(0, 0, 0),albedo=[0.8, 0.2], spec=30)),  #Nariz punto
        Sphere(V3(-3.6, 3.3, -12.1), 1, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Pie
        Sphere(V3(-1.7, 3.3, -12.4), 1, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Pie
        Sphere(V3(4.2, 0.7, -12.2), 1, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Mano
        Sphere(V3(1, 0.7, -12.6), 1, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Mano
        Sphere(V3(3.6, -3, -12.7), 0.7, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Oreja
        Sphere(V3(2, -3, -13), 0.7, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Oreja
        Sphere(V3(1.6, 3.15, -12.1), 0.95, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Pie
        Sphere(V3(3.6, 3.1, -12), 0.95, Material(diffuse=Color(135, 70, 20),albedo=[0.8, 0.2], spec=30)), #Pie
        Sphere(V3(-2.8, -0.82, -13), 0.8, Material(diffuse=Color(199, 144, 90), albedo=[0.8, 0.2], spec=30)), #Nariz
        Sphere(V3(2.8, -0.82, -13), 0.8, Material(diffuse=Color(199, 144, 90), albedo=[0.8, 0.2], spec=30)), #Nariz
        Sphere(V3(-3, 2, -14), 2.35, Material(diffuse=Color(135, 70, 20), albedo=[0.8, 0.2], spec=30)), #Cuerpo
        Sphere(V3(3, 2, -14), 2.35, Material(diffuse=Color(135, 70, 20), albedo=[0.8, 0.2], spec=30)), #Cuerpo
    ]
    r.point(100, 100)
    r.render()
    r.write('RT2.bmp')

def Proyecto2():
    
    #Creación de los materiales
    amarillo_pirámide1 = Material(diffuse=Color(204,174,82), albedo = [1, 1, 0, 0], spec = 50, refractionIndex = 0)
    amarillo_pirámide2 = Material(diffuse=Color(255,217,102), albedo = [1, 1, 0, 0], spec = 50, refractionIndex = 0)
    amarillo_pirámide3 = Material(diffuse = Color(163,139,66), albedo = [1, 1, 0, 0], spec = 50, refractionIndex = 0)
    amarillo_pirámide4 = Material(diffuse = Color(255,225,133), albedo = [1, 1, 0, 0], spec = 50, refractionIndex = 0)
    azul_agua = Material(diffuse=Color(163,199,233), albedo=[0, 0.6, 0, 0.9], spec=70, refractionIndex=2)
    blanco_luna = Material(diffuse = Color(250, 245, 250), albedo=[0.5, 0.4, 0.2, 0.5], spec=126, refractionIndex=1)
    amarillo_suelo = Material(diffuse = Color(255,225,133), albedo = [1, 1, 0, 0], spec = 50, refractionIndex = 0)
    
    
    r = RayTracer(800, 800)
    r.envmap = Envmap('./Proyecto2/envmapNight.bmp')
    r.light = Light(V3(-2, -280, -300), 2, Color(255, 255, 255))
    #Segunda luz a utilizar
    r.light2 = Light(V3( -2, -280, -10),  2,Color(255, 255, 255))
    # r.AmbientLight = AmbientLight(strength= 0.05)
    
    
    #Declaramos las pirámides
    r.scene = [
        Pyramid([V3(-1, 0, -10), V3(-3, -2, -10), V3(-5, 0, -10), V3(-1, 0, -10)], amarillo_pirámide2),
        Pyramid([V3(1, 0, -10), V3(3, -2, -10), V3(5, 0, -10), V3(1, 0, -10)], amarillo_pirámide2),
        Pyramid([V3(-2, 0, -10), V3(-4, -2, -10), V3(-6, 0, -10), V3(-2, 0, -10)], amarillo_pirámide1),
        Pyramid([V3(2, 0, -10), V3(4, -2, -10), V3(6, 0, -10), V3(2, 0, -10)], amarillo_pirámide1),
        Pyramid([V3(0, 0, -10), V3(-2, -2, -10), V3(-4, 0, -10), V3(0, 0, -10)], amarillo_pirámide3),
        Pyramid([V3(0, 0, -10), V3(2, -2, -10), V3(4, 0, -10), V3(0, 0, -10)], amarillo_pirámide3),
        Pyramid([V3(2, 0, -9), V3(0, -3, -9), V3(-2, 0, -9), V3(2, 0, -9)], amarillo_pirámide4),
        Sphere(V3(0, -3, -12), 2, blanco_luna),
        Plane(V3(0, 5, -8),20,20, azul_agua)
    ]
    
    
    r.render()
    r.write('Proyecto2.bmp')

    
    
iterador= False
opciones= 0

while not iterador:
    
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+ BIENVENIDO A MI Raytracer -+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("\n 1) Mostrar RT1 \n 2) Mostrar RT2 " "\n 3) Proyecto 2 \n 4) Salir ")
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