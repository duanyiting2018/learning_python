# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 09:25:48 2021

@author: duanyiting
"""
class student:
    def __init__(self):
        self.name=" "*20
        self.score=0
        self.next=None
front=student()
rear=student()
front=None
rear=None
def enqueue(name,score): #加入数据 
    global front
    global rear
    new_data=student()
    new_data.name=name
    new_data.score=score
    if rear==None:
        front=new_data
    else:
        rear.next=new_data
    rear=new_data
    new_data.next=None
def dequeue(): #取出数据 
    global front
    global rear
    if front==None:
        print("队列已空。")
    else:
        print("姓名：%s\t成绩：%d (取出)"% \
              (front.name,front.score))
        front=front.next
def show():
    global front
    global rear
    ptr=front
    if ptr==None:
        print("队列已空。")
    else:
        while ptr!=None:#从front到rear遍历队列 
            print("姓名：%s\t成绩：%d"% \
              (ptr.name,ptr.score))
            ptr=ptr.next
select=0
while True:
    select=int(input("1加入 2取出 3显示 4离开=>"))
    if select==4:
        break
    if select==1:
        name=input("姓名：")
        score=int(input("成绩："))
        enqueue(name,score)
    elif select==2:
        dequeue()
    elif select==3:
        show()