# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:48:19 2020

@author: duanyiting
"""
global queen
global number
eight=8
queen=[None]*8
number=0
def print_table():
    global number
    x=y=0
    number+=1
    print("")
    print("八皇后问题的第%d组解\t"%number)
    for x in range(eight):
        for y in range(eight):
            if x==queen[y]:
                print("<q>",end="")
            else:
                print("<->",end="")
    print("\n按下任意键继续...\n")
def attack(row,col):
    global queen
    i=0
    atk=0
    offset_row=offset_col=0
    while atk!=1 and i<col:
        offset_col=abs(i-col)
        offset_row=abs(queen[i]-row)
        if queen[i]==row or offset_row==offset_col:
            atk=1
        i+=1
    return atk
def decide_position(value):
    global queen
    i=0
    while i<eight:
        if attack(i,value)!=1:
            queen[value]=i
            if value==7:
                print_table()
            else:
                decide_position(value+1)
        i+=1
decide_position(0)