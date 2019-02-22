# -*- coding: utf-8 -*-
nfile=open("C:/Users/lenovo/Desktop/n1.txt","w")
nfile.write("点名！：\n")
nfile.write("小吴！\n")
nfile.write("小段！")
nfile=open("C:/Users/lenovo/Desktop/n1.txt","r")
print(nfile.readlines())
nfile.close()