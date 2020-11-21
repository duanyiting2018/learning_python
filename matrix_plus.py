# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:23:19 2020

@author: duanyiting
"""
a=[[1,3,5],[7,9,11],[13,15,17]]
b=[[10,30,50],[70,90,110],[130,150,170]]
c=[[119,330,250],[177,666,117],[1233,1250,317]]
N=3
d=[[None]*N for row in range(N)]
for i in range(3):
    for j in range(3):
        d[i][j]=a[i][j]+b[i][j]+c[i][j]
for i in range(3):
    for j in range(3):
        print("%d"%d[i][j],end="\t")