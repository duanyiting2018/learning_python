# -*- coding: utf-8 -*-
from random import choice
nlist=open("C:/Users/lenovo/Desktop/sentence.txt","w")
nlist.write('''crazed,silly,shy,goofy
monkey,elephant,cyclist,teacher
played a ukulele,danced a jig
on the table, at the grocery store,inshower''')
nlist.close()
use=open("C:/Users/lenovo/Desktop/sentence.txt","r")
a=use.readline().split(",")
b=use.readline().split(",")
c=use.readline().split(",")
d=use.readline().split(",")
print(choice(b),choice(a),choice(c),choice(d))
use.close()