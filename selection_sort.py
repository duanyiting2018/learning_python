# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:08:57 2020

@author: duanyiting
"""
def showdata(data):
    for i in range(len(data)):
        print('%5d'%data[i],end=" ")
    print()
    return ""
def select(data):
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            if data[i]>data[j]:
                data[i],data[j]=data[j],data[i]
                print("i:",i," ",data[i],"    ","j:",j," ",data[j])
                showdata(data)
    print()
data=[438,829,73725,35,5,94,23,77]
print("初始数组为:",end="")
showdata(data)
print("\n--------------------------------------------------")
select(data)
print("排序后的数组为:",end="")
showdata(data)