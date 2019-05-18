# -*- coding: utf-8 -*-
a=int(input("输入a："))
b=int(input("输入b："))
c=1
while True:
    if(c%b!=0):
        print(c/b,c)
    c+=1
    if(c>a):
        break