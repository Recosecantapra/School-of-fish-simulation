from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    def __add__(self, other):
        newX = self.__x + other.__x
        newY= self.__y + other.__y
        return Vector(newX,newY)
    
    def __sub__(self,other):
        newX = self.__x - other.__x
        newY= self.__y - other.__y
        return Vector(newX,newY)

    def __mul__(self, k):
       return Vector(self.__x * k, self.__y *k)
    
    def __truediv__(self, k):
        return Vector(self.__x / k, self.__y / k)
 
    def get_length(self):
        return sqrt(self.__x**2 + self.__y**2)
    
    def distance(self,other):
        return (self - other).get_length()
    
    def normalize_vector(self):
        length = self.get_length()
        if length == 0:
            return Vector(0,0)
        return self / length

    def dotProduct(self,vector):
        return (self.__x*vector.__x + self.__y*vector.__y)
   
    def limit(self,maxlimit):
        if self.get_length() > maxlimit:
            return self.normalize_vector()*maxlimit
        else:
            return self
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    


v1 = Vector(2,3)
v2= Vector(1,4)

# whopper hHahahahahxaxaxaxa