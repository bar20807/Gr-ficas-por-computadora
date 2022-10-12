from MathFunctionsMatrix import *
class V3(object):
    def __init__(self, x, y=0, z=0):
        if (type(x) == MathMatrix):
            self.x, self.y, self.z = x.tolist()[0]
        else:    
            self.x=x
            self.y=y
            self.z=z

    
    def round(self):
        self.x=round(self.x)
        self.y=round(self.y)
        self.z=round(self.z)
    
    #Retorna la suma de vectores
    def __add__(self, other):
        return V3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
            )
    
    #Retorna la resta entre vectores
    def __sub__(self, other):
        return V3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
        
    #Retorna la multiplicación entre vectores (escalar)
    def __mul__(self,other):
        #print("SELF: ", self)
        #print("OTHER", other)
        #Evalúa si el tipo de la coordenada es INT
        if (type(other) == int or type(other) == float):
            return V3(
                self.x*other,
                self.y*other,
                self.z*other
            )
            
        #Retorna el producto cruz entre dos vectores de 3 dimensiones
        return V3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
            
    #Retorna el producto punto entre vectores
    """
        Si el producto punto entre dos vectores devuelve 1, es 
        porqué dichos vectores van en la misma dirección.
        
        En caso de que sea -1 es porqué los vectores van 
        en diferente dirección
        
    """
    def __matmul__(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z
        
    #Retorna la magnitud del vector
    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    """
    
        Vector Unitario
        Se conoce como un vector unitario a un vector de largo 1
        
        Es simple trabajar con vectores unitarios en gráficas por computadoras.
        
        Normalización
        Normalizar un vector se refiere a convertirlo en un vector de magnitud 1
            
    """
    def norm(self):
        #Si no devuelve una división por cero
        #print("Entre a Norm")
        try:
            return self * (1 / self.length())
        #Si devuelve una división por cero
        except:
            return V3(-1,-1,-1)
        

    #Retorna los valores en tipo string de las coordenadas ingresadas    
    def __repr__(self):
        return "V3(%s,%s,%s)" % (self.x,self.y,self.z)
    
            
         