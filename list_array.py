# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:31:13 2020

@author: duanyiting
"""
maxstack=100
global stack
stack=[None]*maxstack
top=-1
def isEmpty():
    if top==-1:
        return True
    else:
        return False
def push(data):
    global top
    global maxstack
    global stack
    if top>=maxstack-1:
        print("堆栈已满!")
    else:
        top+=1
        stack[top]=data
def pop():
    global top
    global stack
    if isEmpty():
        print("堆栈为空。")
    else:
        print("弹出的元素为%d"%stack[top])
        top-=1
i=2
count=0
while 1:
    i=int(input("要压入，输1，要弹出，输0，退出输-1:"))
    if i==-1:
        break
    elif i==1:
        value=int(input("请输入元素值:"))
        push(value)
    elif i==0:
        pop()
print("=====================================")
if top<0:
    print("\n堆栈为空。")
else:
    i=top
    while i>=0:
        print("堆栈弹出的顺序是:%d"%stack[i])
        count+=1
        i-=1
    print()
print("=====================================")
