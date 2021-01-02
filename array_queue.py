# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 19:35:06 2021

@author: duanyiting
"""
import sys
MAX=10
queue=[0]*MAX
front=rear=-1
choice=""
while rear<MAX-1 and choice!="e":
    choice=input("【a】加入数值【d】取出数值【e】跳出程序:")
    if choice=="a":
        val=int(input("请输入数值:"))
        rear+=1
        queue[rear]=val
    elif choice=="d":
        if rear>front:
            front+=1
            print("取出数值为:%d"%queue[front])
            queue[front]=0
        else:
            print("队列已空")
            sys.exit()
    else:
        print()
print("-----------------------------------------------")
print("输出队列中所有元素:")
if rear==MAX-1:
    print("队列已满")
elif front>=rear:
    print("没有")
    print("队列已空")
else:
    while rear>front:
        front+=1
        print("[%d]"%queue[front],end=" ")
    print()
    print("-----------------------------------------------")