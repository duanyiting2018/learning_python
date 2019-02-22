# -*- coding: utf-8 -*-
class Triangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def getArea(self):
        return int(self.width*self.height*0.5)
    def __str__(self):
        return str(self.width)+" "+str(self.height)+" "+str(self.getArea())
my_Triangle=Triangle(5,6)
my_Triangle.getArea()
print(my_Triangle)
#------------------------------------------------------------------------------------
class Square:
    def __init__(self,size):
        self.size=size
    def getArea(self):
        return int(self.size**2)
    def __str__(self):
        return str(self.size)+" "+str(self.getArea())
my_Square=Square(8)
my_Square.getArea()
rint(my_Square)