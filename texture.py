import struct as st
def color(r, g, b):
      return bytes([b, g, r])
    
class Texture(object):  
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        image = open(self.path, "rb")
        image.seek(10)
        header_size = st.unpack("=l", image.read(4))[0]
        image.seek(18)
        self.width = st.unpack("=l", image.read(4))[0]
        self.height = st.unpack("=l", image.read(4))[0]
        self.pixels = []
        image.seek(header_size)
        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1))
                g = ord(image.read(1))
                r = ord(image.read(1))
                self.pixels[y].append(color(r,g,b))
        image.close()

    def get_color(self, tx, ty, intensity=1):
        x = int(tx * self.width)
        y = int(ty * self.height)
        try:
            return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.pixels[y][x]))
        except:
            pass