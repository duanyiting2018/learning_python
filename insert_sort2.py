# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:04:53 2020

@author: duanyiting
"""
SIZE=5
def showdata(data):
    for i in range(SIZE):
        print("%3d"%data[i],end=" ")
    print()
def insert(data):
    for i in range(1,SIZE):
        tmp=data[i]
        no=i-1
        while no>=0 and tmp<data[no]:
            data[no+1]=data[no]#把所有元素往后推一个位置 
            no-=1
            showdata(data)
        data[no+1]=tmp
data=[16,25,39,27,12]
print("初始数组为:")
showdata(data)
insert(data)
print("排序后的数组是:")
showdata(data)