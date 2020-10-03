# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 18:56:32 2020

@author: duanyiting
"""
class student:
    def __init__(self):
        self.name=""
        self.score=0
        self.next=None
head=student()
head.next=None
ptr=head
select=0
while select !=2:
    print("输入1添加数据,输入2离开:")
    select=int(input())
    if select==1:
        new_data=student()
        new_data.name=input("学生姓名:")
        new_data.no=input("学生学号:")
        new_data.Math=input("数学成绩:")
        new_data.English=input("英语成绩:")
        ptr.next=new_data#指针设置为新元素的位置 
        new_data.next=None#下一个元素先指向None
        ptr=ptr.next