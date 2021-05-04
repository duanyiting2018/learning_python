# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:31:02 2021

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
        if ptr==None:
            return None
        if ptr.data==val:
            return ptr
        elif ptr.data>val:
            ptr=ptr.left
        else:
            ptr=ptr.right
        i+=1
def inorder(ptr):
    if ptr!=None:
        inorder(ptr.left)
        print("[%2d] "%ptr.data,end="")
        inorder(ptr.right)
arr=[7,1,4,2,8,13,12,11,15,9,5]
ptr=None
print("初始数组:")
for i in range(11):
    ptr=create_tree(ptr,arr[i])
    print("[%2d] "%arr[i],end="")
print()
data=int(input("请输入要新增的节点:"))
if search(ptr,data)!=None:
    print("二叉树中已有此节点了。")
else:
    ptr=create_tree(ptr,data)
    inorder(ptr)