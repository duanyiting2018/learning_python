# -*- coding: utf-8 -*-
class Ball:
    def bounce(self):
        if self.direction=="down":
            self.direction="up"
myBall=Ball()
myBall.direction="down"
myBall.colour="red"
myBall.size="small"
print("I just created a ball.")
print("My ball is:",myBall.size)
print("My ball is:",myBall.colour)
print("My ball's direction is",myBall.direction)
print("Now I'm going to bounce the ball.")
print()
myBall.bounce()
print("Now the ball's direction is:",myBall.direction)
# ========================================================================
#                                                                        #
# ========================================================================
class Ball:
    def __init__(self,colour,size,direction):
        self.colour=colour
        self.size=size
        self.direction=direction
    def bounce(self):
        if self.direction=="down":
            self.direction="up"
myBall=Ball("red","small","down")
myBall.direction="down"
myBall.colour="red"
myBall.size="small"
print("I just created a ball.")
print("My ball is:",myBall.size)
print("My ball is:",myBall.colour)
print("My ball's direction is",myBall.direction)
print("Now I'm going to bounce the ball.")
print()
myBall.bounce()
print("Now the ball's direction is:",myBall.direction)