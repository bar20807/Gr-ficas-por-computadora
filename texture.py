import struct as st
def color(r,g,b):
    return bytes([
        int(b*255), #Se multiplica el número ingresado por 255 para obtener el color
        int(g*255),
        int(r*255)])
class Texture:  
    def read(self,path):
        with open(path,"rb") as image:
            image.seek(2+4+2+2)
            #Lee un total de 4 bites
            #unpack sirve para darle un valor entero a los bites
            header_size=st.unpack("=l",image.read(4))[0]
            image.seek(2+4+2+2+4+4)
            #Creamos el ancho y alto de la imagen
            self.width=st.unpack("=l",image.read(4))[0]
            self.height=st.unpack("=l",image.read(4))[0]
            
            #Ahora leemos dicho archivo            
            image.seek(header_size)
            
            self.pixels=[]
            
            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b=ord(image.read(1))
                    g=ord(image.read(1))
                    r=ord(image.read(1))
                    self.pixels[y].append(
                        color((r/255),(g/255),(b/255))
                    )
    #Tomamos el color que se encuentra en cierta posición de nuestro array
    def get_color(self,tx,ty):
        x= round(tx*self.width)
        y= round(ty*self.height)
        return self.pixels[y][x]
    #Obtenemos el color del array con cierta intensidad
    def get_color_with_intensity(self,tx,ty,intensity):
        x= round(tx*self.width/255)
        y= round(ty*self.height/255)
        
        print("VALOR DE X ", x)
        print("VALORES DE Y", y)
        print("VALORES DE r", self.pixels[y][x][0]*intensity)
        r= self.pixels[y*255][x*255][0]*intensity
        #print("VALORES DE r", r)
        g= self.pixels[y*255][x*255][1]*intensity
        b= self.pixels[y*255][x*255][2]*intensity
        
        return color((r/255),(g/255),(b/255))