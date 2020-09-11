# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 20:42:21 2020

@author: duanyiting
"""
import random
def inputarr(data,size):
    for i in range(size):
        data[i]=random.randint(1,100)
def showdata(data,size):
    for i in range(size):
        print("%4d"%data[i],end="")
    print()
def quick(d,size,lf,rg):
    if lf<rg:
        lf_idx=lf+1
        while d[lf_idx]<d[lf]:
            if lf_idx+1>size:
                break
            lf_idx+=1
        rg_idx=rg
        while d[rg_idx]>d[lf]:
            rg_idx-=1
        while lf_idx<rg_idx:
            d[lf_idx],d[rg_idx]=d[rg_idx],d[lf_idx]
            lf_idx+=1
            while d[lf_idx]<d[lf]:
                lf_idx+=1
            rg_idx-=1
            while d[rg_idx]>d[lf]:
                rg_idx-=1
        d[lf],d[rg_idx]=d[rg_idx],d[lf]
        
        for i in range(size):
            print("%3d"%d[i],end="")
        print()
        
        quick(d,size,lf,rg_idx-1)
        quick(d,size,rg_idx+1,rg)
data=[0]*100
size=int(input("请输入数组的大小:"))
inputarr(data,size)
print("输入为:")
showdata(data,size)
print("排序过程如下:")
quick(data,size,0,size-1)
print("排序结果为:")
showdata(data,size)