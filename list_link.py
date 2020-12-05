# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 18:09:09 2020

@author: duanyiting
"""
class Node:
    def __init__(self):
        self.data=0
        self.next=None
top=None
def isEmpty():
    global top
    if top==None:
        return True
    else:
        return False
def push(data):
    global top
    new_node=Node()
    new_node.data=data
    new_node.next=top
    top=new_node
def pop():
    global top
    if isEmpty():
        print("堆栈为空。")
        return -1
    else:
        ptr=top#指向堆栈的顶端 
        top=top.next#将堆栈顶部的指针指向下一个节点 
        temp=ptr.data#弹出堆栈的数据 
        return temp#将从堆栈弹出的数据返回给主程序 
while 1:
    i=int(input("要压入，输1，要弹出，输0，退出输-1:"))
    if i==-1:
        break
    elif i==1:
        value=int(input("请输入元素值:"))
        push(value)
    elif i==0:
        print("弹出的元素为%d"%pop())
print("=====================================")
while not isEmpty():
    print("堆栈弹出的顺序为%d"%pop())
print("=====================================")
