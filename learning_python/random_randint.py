# -*- coding: utf-8 -*-
from random import randint
ts=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
    d_t=randint(2,14)
    ts[d_t]+=1
for i in range(2,15):
    print("t",i,"c u",ts[i],"tis.")
print()
print()
print()
from random import randint
ts=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
    die1=randint(1,7)
    die2=randint(1,7)
    d_t=die1+die2
    ts[d_t]+=1
for i in range(2,15):
    print("t",i,"c u",ts[i],"tis.")