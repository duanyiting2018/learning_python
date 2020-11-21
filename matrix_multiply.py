# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:26:41 2020

@author: duanyiting
"""
def MatrixMultiply(arrA,arrB,arrC,M,N,P):
    global C
    if M<=0 or N<=0 or P<=0:
        print("数据错误,请修改")
        return
    for i in range(M):
        for j in range(P):
            Temp=0
            for k in range(N):
                Temp=Temp+int(arrA[i*N+k])*int(arrB[k*P+j])
            arrC[i*P+j]=Temp
print("请输入矩阵a的维数:")
M=int(input("M= "))
N=int(input("N= "))
A=[None]*M*N
print("请输入a的各个元素:")
for i in range(M):
    for j in range(N):
        A[i*N+j]=input("a%d%d="%(i,j))
print("请输入矩阵b的维数:")
N=int(input("N= "))
P=int(input("P= "))
B=[None]*N*P
print("请输入b的各个元素:")
for i in range(N):
    for j in range(P):
        B[i*P+j]=input("b%d%d="%(i,j))
C=[None]*M*P
MatrixMultiply(A,B,C,M,N,P)
print("A*B是:")
for i in range(M):
    for j in range(P):
        print("%d"%C[i*P+j],end="\t")
    print()
 