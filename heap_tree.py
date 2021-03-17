# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:43:28 2021

@author: lenovo
"""
def heap(data,size):
    for i in range(int(size/2),0,-1):
        ad_heap(data,i,size-1)
    print()
    print("堆积的内容：",end="")
    for i in range(1,size):
        print("[%2d] "%data[i],end="")
    print('\n')
    for i in range(size-2,0,-1):
        #头尾节点交换 
        data[i+1],data[1]=data[1],data[i+1]
        ad_heap(data,1,i)
        print("处理过程为：",end="")
        for j in range(1,size):
            print('[%2d] '%data[j],end="")
        print()
def ad_heap(data,i,size):
    j=2*i
    tmp=data[i]
    post=0
    while j<=size and post==0:
        if j<size:
            if data[j]<data[j+1]:#找出最大节点 
                j+=1
        if tmp>=data[j]:#若树根打，则结束比较过程 
            post=1
        else:
            data[int(j/2)]=data[j]
            j=2*j
    data[int(j/2)]=tmp#让树根为父节点 
data=[0,5,6,10,4,7,3,9,1,2,8]
size=11
print('初始数组为：',end="")
for i in range(1,size):
    print('[%2d] '%data[i],end="")
heap(data,size)
print('排序结果为：',end="")
for i in range(1,size):
    print('[%2d] '%data[i],end="")