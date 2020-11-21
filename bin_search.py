# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 19:58:44 2020

@author: duanyiting
"""
import random
def bin_search(data,val):
    low=0
    high=99
    while low <= high and val !=-1:
        mid=int((low+high)/2)
        if val<data[mid]:
            print("%d介于位置%d[%4d]和中间值%d[%4d]之间,找左半边" \
                  %(val,low+1,data[low],mid+1,data[mid]))
            high=mid-1
        elif val>data[mid]:
            print("%d介于位置%d[%4d]和中间值%d[%4d]之间,找右半边" \
                  %(val,mid+1,data[mid],high+1,data[high]))
            low=mid+1
        else:
            return mid
    return -1
val=1
data=[0]*100
for i in range(100):
    data[i]=val
    val=val+random.randint(1,5)
while True:
    num=0
    val=int(input("请输入查找键值(1~100),输入-1结束:"))
    if val==-1:
        break
    num=bin_search(data,val)
    if num==-1:
        print("####没有找到[%4d]####"%val)
    else:
        print("在第%2d个位置找到[%4d]"%(num+1,data[num]))
print("数据内容为:")
for i in range(5):
    for j in range(10):
        print("%4d %4d"%(i*10+j+1,data[i*10+j]),end=" ")
    print()
