# -*- coding: utf-8 -*-
import random
class WhiteBlackBall:
    def __init__(self,white_Number,black_Number):
        self.white_Number = white_Number
        self.black_Number = black_Number
        
    def takeBall(self,take_white_N,take_black_N):
        # 取0白2黑：
        if take_white_N == 0 and take_black_N == 2 :            
            self.black_Number = self.black_Number - 2
            self.black_Number =self.black_Number + 1
            
        # 取2白0黑：
        if take_white_N == 2 and take_black_N == 0 :  
            self.white_Number = self.white_Number - 2
            self.black_Number =self.black_Number + 1
            
         #取1白1黑：
        if take_white_N == 1 and take_black_N == 1 :           
            self.white_Number = self.white_Number - 1
            self.black_Number =self.black_Number - 1        
            self.white_Number = self.white_Number + 1  

#取球的各种情况：2白0黑，0白2黑，1白1黑
take_Situation=[[2,0],[0,2],[1,1]]
      
print("初始化：99个白球 100个黑球")
whiteBlackBall=WhiteBlackBall(99,100)
for i in range(1,198):
    if whiteBlackBall.black_Number >= 0 and  whiteBlackBall.white_Number >= 0 : 
        # 当取到只剩下1个白球的时候，此时不能取2个白球了，只能随机取：0白2黑，1白1黑
        if whiteBlackBall.white_Number == 1 :
                take_index = random.randint(1, 2)  
                take_white_number=take_Situation[take_index][0]
                take_black_bumber=take_Situation[take_index][1] 
        # 白球不止1个的时候，可以取2白0黑，0白2黑，1白1黑
        if  whiteBlackBall.white_Number > 1 :  
                take_index = random.randint(0, 2)  
                take_white_number=take_Situation[take_index][0]
                take_black_bumber=take_Situation[take_index][1] 
    
        whiteBlackBall.takeBall(take_white_number,take_black_bumber)
        print("第{}次随机取 {}个白球{}个黑球，此时的白球个数{}，黑球个数{}"
              .format(i,take_white_number,take_black_bumber,
              whiteBlackBall.white_Number,whiteBlackBall.black_Number))