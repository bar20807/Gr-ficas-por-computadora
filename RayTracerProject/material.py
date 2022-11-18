from msilib.schema import Class


class Material(object):
    def __init__(self, diffuse, albedo, spec, refractionIndex = 0):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractionIndex = refractionIndex
        
        