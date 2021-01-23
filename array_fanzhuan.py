# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 21:55:30 2020

@author: duanyiting
"""
class employee():
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=""
        self.next=None
findword=0
namedata1=["Anney","Scott","Marry","Jon","Mark", \
           "Ricky","Lisa","Alice","Bob","Jack","Ann","Danny"]
data=[[1001,10000],[1002,20000],[1003,30000],[1004,40000], \
      [1005,50000],[1006,60000],[1007,70000],[1008,80000], \
      [1009,90000],[1010,10000],[1011,50000],[1012,70000]]
head=employee()
if not head:
    print("Error!!!")
head.num=data[0][0]
head.name=namedata1[0]
head.salary=data[0][1]
head.next=None
ptr=head
for i in range(1,12):
    newnode=employee()
    newnode.num=data[i][0]
    newnode.name=namedata1[i]
    newnode.salary=data[i][1]
    newnode.next=None
    ptr.next=newnode
    ptr=ptr.next
ptr=head
i=0
print("反转前的员工链表:")
while ptr!=None:
    print("[%2d %6s %3d] =>"%(ptr.num,ptr.name,ptr.salary),end="")
    i+=1
    if i>=3:
        print()
        i=0
    ptr=ptr.next
ptr=head
before=None
print("反转后的员工链表:")
while ptr!=None:
    last=before
    before=ptr
    ptr=ptr.next
    before.next=last
ptr=before
while ptr!=None:
    print("[%2d %6s %3d] =>"%(ptr.num,ptr.name,ptr.salary),end="")
    i+=1
    if i>=3:
        print()
        i=0
    ptr=ptr.next