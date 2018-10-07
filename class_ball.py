# -*- coding: utf-8 -*-
class Ball:
    def __init__(self,colour,size,direction):
        self.colour=colour
        self.size=size
        self.direction=direction
    def __str__(self):
        msg="Hi,I'm a"+" "+self.size+" "+self.colour+" "+"ball!"
        return msg
myBall=Ball("red","small","down")
print(myBall)