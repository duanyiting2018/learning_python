# -*- coding: utf-8 -*-
nlist=open("C:/Users/lenovo/Desktop/n1.txt","a")
nlist.write("\n你们不听话就要打！")
nlist=open("C:/Users/lenovo/Desktop/n1.txt","r")
print(nlist.readlines())
nlist.close()