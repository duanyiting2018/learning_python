# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:37:47 2020

@author: duanyiting
"""
def count_n_o():
    string="want you to know one thing no i want t"
    t1=0
    t2=0
    for i in range(len(string)):
        if string[i]=="n":
            t1+=1
        elif string[i]=="o":
            t2+=1
    return str(t1)+" "+str(t2)
print(count_n_o())