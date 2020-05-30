# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:13:00 2020

@author: duanyiting
"""
data=[]
print("冒泡排序,请输入8个数：")
for i in range(0,8):
    data.append(int(input()))
print()
for i in range(7,-1,-1):
    for j in range(i):
        if data[j]>data[j+1]:#比较,交换的次数 
            data[j],data[j+1]=data[j+1],data[j]
    print("第%d次排序的结果是："%(8-i),end=' ')
    for j in range(8):
        print('%1d'%data[j],end=' ')
    print()
print("排序的结果是：")
for j in range(8):
    print('%1d'%data[j],end=' ')
print()