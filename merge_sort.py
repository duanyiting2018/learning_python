# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:14:11 2020

@author: duanyiting
"""
list1=[20,45,51,88,99999]#99999是数组的结束数字不列入排序 
list2=[98,10,23,15,99999]#99999是数组的结束数字不列入排序 
list3=[]
def merge_sort(list1,list2):
    select_sort(list1,len(list1)-1)
    select_sort(list2,len(list2)-1)
    print("\n第1个数组的排序结果是:",end="")
    for i in range(len(list1)-1):
        print(list1[i],end="")
    print("\n第2个数组的排序结果是:",end="")
    for i in range(len(list1)-1):
        print(list2[i],end="")
    for i in range(100):
        print("=",end="")
    My_Merge(len(list1)-1,len(list2)-1)
    for i in range(100):
        print("=",end="")
    print("\n排序最终结果为:",end="")
    for i in range(len(list1)+len(list2)-2):
        print(" %d"%list3[i],end="")
def select_sort(data,size):
    for base in range(size-1):
        small=base
        for j in range(base+1,size):
            if data[j]<data[small]:
                small=j
        data[small],data[base]=data[base],data[small]
def My_Merge(size1,size2):
    global list1
    global list2
    global list3
    index1=0
    index2=0
    for index3 in range(len(list1)+len(list2)-2):
        if list1[index1]<list2[index2]:
            list3.append(list1[index1])
            index1+=1
            print("此数字%d属于第1个数组"%list3[index3])
        else:
            list3.append(list2[index2])
            index2+=1
            print("此数字%d属于第2个数组"%list3[index3])
        print("目前排序结果为:",end="")
        for i in range(index3+1):
            print(list3[i]," ",end="")
        print("\n")
merge_sort(list1,list2)