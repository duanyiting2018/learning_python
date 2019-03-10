# -*- coding: utf-8 -*-
from random import choice
coin=["Heads","Tails"]
h_i_r=0
t=0
for i in range(1000000):
    if choice(coin)=="Heads":
        h_i_r+=1
    else:
        h_i_r=0
    if h_i_r==10:
        t+=1
        h_i_r=0
print("W g 10 h i a r",t,"tis.")