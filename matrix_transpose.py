# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:23:19 2020

@author: duanyiting
"""
a=[[119,330,250],[177,666,117],[1233,1250,317]]
N=3
b=[[None]*N for row in range(N)]
print("原矩阵是:")
for i in range(3):
    for j in range(3):
        print("%d"%a[i][j],end="\t")
    print()
for i in range(3):
    for j in range(3):
        b[i][j]=a[j][i]
print()
print("转置后的矩阵是:")
for i in range(3):
    for j in range(3):
        print("%d"%b[i][j],end="\t")
    print()