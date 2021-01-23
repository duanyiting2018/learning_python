# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:50:08 2021

@author: duanyiting
"""
def tree_create(tree,data,lenth):
    for i in range(1,lenth):
        level=1
        while tree[level]!=0:
            if data[i]>tree[level]:#如果数组内的值大于根,则往左子树比较 
                level=level*2+1
            else:#反之则往右子树比较 
                level=level*2
        tree[level]=data[i]
lenth=9
data=[0,6,3,5,4,7,8,9,2]
tree=[0]*16
print("初始数组:")
for i in range(lenth):
    print("%d "%data[i],end="")
print("")
tree_create(tree,data,lenth)
print("二叉树内容:")
for i in range(1,16):
    print("%d "%tree[i],end="")
print()