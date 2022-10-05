import struct

class ReadObj(object):
    def __init__(self,filename):
        with open(filename) as f:
            self.lines=f.read().splitlines()
        self.vertices=[]
        self.tvertices=[]
        self.faces=[]
        
        for line in self.lines:
            if not line or line.startswith('#'):
                continue
                
            prefix, value=line.split(' ', 1)
            
            #Ver que valores devuelve la lectura del archivo.
            #print("Value: ",value)
            
            if prefix == 'v':
                self.vertices.append(
                    list(
                    map(
                        float, value.strip().split(' ')
                        )
                    )
                )
            if prefix == 'vt':
                self.tvertices.append(
                    list(
                    map(
                        float, value.strip().split(' ')
                        )
                    )
                )
            if prefix == 'f':
                try: 
                    self.faces.append(
                        [
                            list(
                                map(int, face.strip().split('/') 
                                )
                            ) 
                            for face in value.strip().split(' ') 
                        ]
                    )
                except:
                    self.faces.append(
                        [
                            list(
                                map(int, face.strip().split('//')
                                )
                            ) 
                            for face in value.strip().split(' ') 
                        ]
                    )