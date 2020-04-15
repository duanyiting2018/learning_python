# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:52:40 2020

@author: duanyiting
"""
flag=0
h=[]
num=int(input("num:"))
for i in range(1,num+1):
    h.append(int(input("h[i]:")))
n=num
def swap(x,y):
    global h
    t=h[x-1]
    h[x-1]=h[y-1]
    h[y-1]=t
    return
def down(i):
    global flag
    global h
    while(i*2<=n and flag==0):
        if(h[i-1]<h[i*2-1]):
            t=i*2
        else:
            t=i
        if(i*2+1<=n):
            if(h[t-1]<h[i*2]):
                t=i*2+1
        if(t!=i):
            swap(t,i)
            i=t
        else:
            flag=1
    return
def creat():
    for i in range(int(n/2),0,-1):
        down(i)
    return
def heapsort():
    global n
    while(n>1):
        swap(1,n)
        n=n-1
        down(1)
    return
creat()
heapsort()
for i in range(1,num+1):
    print(h[i-1],end=' ')