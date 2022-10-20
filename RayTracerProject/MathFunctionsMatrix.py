from Vector import *
from array import *
class MathMatrix(object):
    def __init__(self, matrix: array):
        self.matrix = matrix

    """
        Referencias para la lógica suma de matrices:
        https://www.youtube.com/watch?v=CDozWggBP6Y&ab_channel=ManuelGonz%C3%A1lez
    
    """
    
    def __add__(self, other):
        if (len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])):
            c=[]
            for i in range(len(self.matrix)):
                c.append([])
                for j in range(len(self.matrix[0])):
                    c[i].append(self.matrix[i][j] + other.matrix[i][j])
            
            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return MathMatrix(c)
        else:
            return None


    def __sub__(self, other):
        if (len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])):
            c=[]
            for i in range(len(self.matrix)):
                c.append([])
                for j in range(len(self.matrix[0])):
                    c[i].append(self.matrix[i][j] - other.matrix[i][j])
            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return MathMatrix(c)
        else:
            return None


    # def mul(v0, k):
    #   return V3(v0.x * k, v0.y * k, v0.z *k)

    """ 
    Referencias para la lógica de multiplicación de matrices:
        https://www.youtube.com/watch?v=IbzzK9PtFBE&ab_channel=ManuelGonz%C3%A1lez 
    
    """
    
    def __mul__(self, other):
        c=[]
        """if (len(other.matrix)!=len(self.matrix[0])):
            print ("Este es el valor de other: " + str(other.matrix))
            print("Len de other: " + str(len(other.matrix)))
            print("Len de self: " + str(len(self.matrix[0])))"""
            
        if len(self.matrix[0]) == len(other.matrix):
            c = []
            for i in range(len(self.matrix)):
                c.append([])
                for j in range(len(other.matrix[0])): 
                    c[i].append(0)

            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        c[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return MathMatrix(c)
        else:
            return None

    def getMathMatrix(self):
        return self.matrix
        