# -*- coding: utf-8 -*-
class AI:
    def __init__(self):
        pass
    def tune(self):
        if self.robot.lookInFront()=="bot":
            self.robot.attack()
        else:
            self.goward(self.robot.locateEnemy()[0])
    def goward(self,enemy):
        my=self.robot.position
        de=(enemy[0]-my[0],enemy[1]-my[1])
        if abs(de[0])>abs(de[1]):
            if de[0]<0:
                tot=3
            else:
                tot=1
        else:
            if de[1]<0:
                tot=0
            else:
                tot=2
        if self.robot.rotation==tot:
            self.robot.goForth()
        else:
            ltn=(self.robot.rotation-tot)%4
            if ltn<=2:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()