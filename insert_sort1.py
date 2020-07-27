# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:05:50 2020

@author: duanyiting
"""
size=8
def showdata(data2):
    for i in range(size):
        print('%1d'%data2[i],end=' ')
    print()
def insert_sort(data3):
    for i in range(1,size):
        tmp=data3[i]#tmp用来暂存数据 
        no=i-1
        while no>=0 and tmp<data3[no]:
            data3[no+1]=data3[no]#将所有元素后移1位 
            no=no-1
        data3[no+1]=tmp#最小的元素放在data3[0] 
data1=[]
print("插入排序,请输入8个数：")
for i in range(0,8):
    data1.append(int(input()))
#showdata(data1)
insert_sort(data1)
print("排序后的数组是：")
showdata(data1)