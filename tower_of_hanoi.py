# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:32:43 2020

@author: duanyiting
"""
def hanoi(n,p1,p2,p3):
    if n==1:
        print("盘子从%d移到%d"%(p1,p3))
    else:
        hanoi(n-1,p1,p3,p2)
        print("盘子从%d移到%d"%(p1,p3))
        hanoi(n-1,p2,p1,p3)
j=int(input("请输入要移动盘子的数量:"))
hanoi(j,1,2,3)