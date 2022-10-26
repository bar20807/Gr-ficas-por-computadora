class Color(object):
    def __init__(self, r, g, b):
        self.r = min(255, max(r, 0))
        self.g = min(255, max(g, 0))
        self.b = min(255, max(b, 0))
        
    def __mul__(self, other):
        
        r = self.r
        g = self.g
        b = self.b
        
        if(type(other) == int or type(other) == float):
            r *= other
            g *= other
            b *= other
        else:
            r *= other.r
            g *= other.g
            b *= other.b
        
        r = min(255, max(r, 0))
        g = min(255, max(g, 0))
        b = min(255, max(b, 0))
        
        return Color(r,g,b)
    
    def __add__(self, other):
        
        r = self.r
        g = self.g
        b = self.b
        
        if(type(other) == int or type(other) == float):
            r += other
            g += other
            b += other
        else:
            r += other.r
            g += other.g
            b += other.b
        
        r = min(255, max(r, 0))
        g = min(255, max(g, 0))
        b = min(255, max(b, 0))
        
        return Color(r,g,b)
    
    def toBytes(self): 
        return bytes([int(self.b), int(self.g), int(self.r)])
    
    def __repr__(self):
        return "color(%s, %s, %s)" % (self.r, self.g, self.b)
    
        
        