# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:12:19 2021

@author: duanyiting
"""
class tree:
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None
def create_tree(root,val):
    newnode=tree()
    newnode.data=val
    newnode.left=None
    newnode.right=None
    if root==None:
        root=newnode
        return root
    else:
        current=root
        while current!=None:
            backup=current
            if current.data>val:
                current=current.left
            else:
                current=current.right
        if backup.data>val:
            backup.left=newnode
        else:
            backup.right=newnode
    return root
def search(ptr,val):
    i=1
    while True:
        if ptr==None:#如果没找到就返回None
            return None
        if ptr.data==val:#节点值等于查找值 
            print("共查找%d次"%i)
            return ptr
        elif ptr.data>val:#节点值大于查找值 
            ptr=ptr.left
        else:#节点值小于查找值 
            ptr=ptr.right
        i+=1
arr=[7,1,4,2,8,13,12,11,15,9,5]
ptr=None
print("初始数组:")
for i in range(11):
    ptr=create_tree(ptr,arr[i])
    print("[%2d] "%arr[i],end="")
print()
while True:
    data=int(input("请输入查找值，输0退出:"))
    if search(ptr,data)!=None:
        print("你要找的值[%3d]找到了。"%data)
    elif data==0:
        break
    else:
        print("值未找到！")