# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:58:55 2021

@author: lenovo
"""
maxsize=10
front=-1
rear=-1
class Node:
    def __init__(self,x):
        self.x=x
        self.next=None
class graphlink:
    def __init__(self):
        self.first=None
        self.last=None
    def my_print(self):
        current=self.first
        while current!=None:
            print("[%d] "%current.x,end="")
            current=current.next
        print()
    def insert(self,x):
        newnode=Node(x)
        if self.first==None:
            self.first=newnode
            self.last=newnode
        else:
            self.last.next=newnode
            self.last=newnode
def enqueue(value):
    global maxsize
    global rear
    global queue
    if rear>=maxsize:
        return
    rear+=1
    queue[rear]=value
def dequeue():
    global front
    global queue
    if front==rear:
        return -1
    front+=1
    return queue[front]
def bfs(current):
    global front
    global rear
    global Head
    global run
    enqueue(current)
    run[current]=1
    print("[%d]"%current,end="")
    while front!=rear:
        current=dequeue()
        tempnode=Head[current].first
        while tempnode!=None:
            if run[tempnode.x]==0:
                enqueue(tempnode.x)
                run[tempnode.x]=1
                print("[%d]"%tempnode.x,end="")
            tempnode=tempnode.next
data=[[0]*2 for row in range(20)]
data=[[1,2],[2,1],[1,3],[3,1],[2,4], \
     [4,2],[2,5],[5,2],[3,6],[6,3], \
     [3,7],[7,3],[4,5],[5,4],[6,7], \
     [7,6],[5,8],[8,5],[6,8],[8,6]]
run=[0]*9
queue=[0]*maxsize
Head=[graphlink]*9
print("图的邻接表内容：")
for i in range(1,9):
    run[i]=0
    print("顶点 %d => "%i,end="")
    Head[i]=graphlink()
    for j in range(20):
        if data[j][0]==i:
            datanum=data[j][1]
            Head[i].insert(datanum)
    Head[i].my_print()
print("bfs的顶点：")
bfs(1)
print()