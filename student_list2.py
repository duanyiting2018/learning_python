# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:09:55 2020

@author: duanyiting
"""
import sys
import random
def concatlist(ptr1,ptr2):
    ptr=ptr1
    while ptr.next!=None:
        ptr=ptr.next
    ptr.next=ptr2
    return ptr1
class employee:
    def __init__(self):
        self.sum=0
        self.salary=0
        self.name=""
        self.next=None
findword=0
data=[[None]*2 for row in range(12)]
namedata1=["Amy","Sally","Marry","John" \
           ,"Mark","Rose","Lisa","Jack" \
           ,"Hanson","Almy","Bob","Jon"]
namedata2=["Amya","Sallys","Marrym","Johnj" \
           ,"Markm","Roser","Lisal","Jackj" \
           ,"Hansonh","Almya","Bobb","Jon"]
for i in range(12):
    data[i][0]=i+1
    data[i][1]=random.randint(51,100)
head1=employee()
if not head1:
    print("操作失败,请重试")
    sys.exit(0)
head1.num=data[0][0]
head1.name=namedata1[0]
head1.salary=data[0][1]
head1.next=None
ptr=head1
for i in range(1,12):
    newnode=employee()
    newnode.num=data[i][0]
    newnode.name=namedata1[i]
    newnode.salary=data[i][1]
    newnode.next=None
    ptr.next=newnode
    ptr=ptr.next
for i in range(12):
    data[i][0]=i+13
    data[i][1]=random.randint(51,100)
head2=employee()
if not head2:
    print("操作失败,请重试")
    sys.exit(0)
head2.num=data[0][0]
head2.name=namedata2[0]
head2.salary=data[0][1]
head2.next=None
ptr=head2
for i in range(1,12):
    newnode=employee()
    newnode.num=data[i][0]
    newnode.name=namedata2[i]
    newnode.salary=data[i][1]
    newnode.next=None
    ptr.next=newnode
    ptr=ptr.next
i=0
ptr=concatlist(head1,head2)
print("两个链表相连的结果是:")
while ptr!=None:
    print("[%2d %6s %3d]=>"%(ptr.num,ptr.name,ptr.salary),end="")
    i+=1
    if i>=3:
        print()
        i=0
    ptr=ptr.next