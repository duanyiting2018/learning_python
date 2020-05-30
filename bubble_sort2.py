# -*- coding: utf-8 -*-
"""
Created on Sat May 30 08:29:29 2020

@author: duanyiting
"""
data=[89,28,4,857,728,89,29,7]
print("冒泡排序,初始数组为:")
for i in range(len(data)):
    print(" ",data[i],end="")
print()
for i in range(len(data)-1,-1,-1):
    for j in range(i):
        if data[j]>data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]
    print("第%d组排序结果:"%(len(data)-i),end="")
    for j in range(len(data)):
        print(" ",data[j],end="")
    print()
print("排序后的结果:")
for i in range(len(data)):
    print(" ",data[i],end="")
print()