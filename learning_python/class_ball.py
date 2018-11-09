# -*- coding: utf-8 -*-
class Ball:
    def __init__(self,colour,size,direction):
        self.colour=colour
        self.size=size
        self.direction=direction
    def __str__(self):
        msg="Hi,I'm a "+self.size+" "+self.colour+" "+"ball,and it's "+self.direction+"."
        return msg
    def bounce(self):
        print("ball bounce.")
myBall=Ball("red","small","down")
myBall.bounce()
Ball.around()
print(myBall)
Ball2=Ball("blue","big","up")
print("Hi,I'm a small red ball,and it's up.")