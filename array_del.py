# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:05:41 2020

@author: duanyiting
"""
import sys
class employee():
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=""
        self.next=None
def del_ptr(head,ptr):
    top=head
    if ptr.num==head.num:
        head=head.num
        print("已删除第 %d 号员工 姓名：%s 薪水：%d" \
              %(ptr.num,ptr.name,ptr.salary))
    else:
        while top.next!=ptr:
            top=top.next
        if ptr.next==None:
            top.next=None
            print("已删除第 %d 号员工 姓名：%s 薪水：%d" \
            %(ptr.num,ptr.name,ptr.salary))
        else:
            top.next=ptr.next
            print("已删除第 %d 号员工 姓名：%s 薪水：%d" \
            %(ptr.num,ptr.name,ptr.salary))
    return head
findword=0
namedata=["a","b","c","d","e","f","g","h","i","j","k","l"]
data=[[1001,57859],[1002,48032],[1003,49783],[1004,58189],[1005,39809], \
      [1006,49128],[1007,43985],[1008,39875],[1009,63753],[1010,50298], \
      [1011,29189],[1012,64021]]
print("员工编号 工薪 员工编号 工薪 员工编号 工薪 员工编号 工薪")
print("sbsbsbsbsbsbsbsbsbsbsbsbssbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsb")
for i in range(3):
    for j in range(4):
        print("%2d [%3d] "%(data[j*3+i][0],data[j*3+i][1]),end="")
    print()
head=employee()
if not head:
    print("Error!!!")
    sys.exit(0)
head.num=data[0][0]
head.name=namedata[i]
head.salary=data[0][1]
head.next=None
ptr=head
for i in range(1,12):
    newnode=employee()
    newnode.num=data[i][0]
    newnode.name=namedata[i]
    newnode.salary=data[i][1]
    newnode.next=None
    ptr.next=newnode
    ptr=ptr.next
while(1):
    findword=int(input("请输入要删除的员工编号,退出输入-1："))
    if(findword==-1):
        break
    else:
        ptr=head
        find=0
        while ptr!=None:
            if ptr.num==findword:
                ptr=del_ptr(head,ptr)
                find=find+1
                head=ptr
            ptr=ptr.next
        if find==0:
            print("没有找到!!!")
ptr=head
print("\t员工编号   姓名\t薪水")
print("sbsbsbsbsbsbsbsbsbsbsbsbssbsbsbsbsb")
while(ptr!=None):
    print("\t[%d]\t[ %-3s]\t[%3d]"%(ptr.num,ptr.name,ptr.salary))
    ptr=ptr.next