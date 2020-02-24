# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:33:37 2020

@author: duanyiting
"""
def showdata(data2):
    for i in range(8):
        print('%3d'%data2[i],end=' ')
    print()
def select(data3):
    for i in range(7):
        for j in range(i+1,8):
            if data3[i]>data3[j]:#比较第i和j个元素 
                data3[i],data3[j]=data3[j],data3[i]
    print()
data1=[]
print("选择排序,请输入8个数：")
for i in range(0,8):
    data1.append(int(input()))
select(data1)
print("排序后的数组是：")
for i in range(8):
    print('%1d'%data1[i],end=' ')
print()