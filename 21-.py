# -*- coding: utf-8 -*-
print("Hi",end=" ")
print("There")

print("Hi"+"There")

print("ABC\tDEF\tGHI")

print("H\\I")

dec=5.123456
print("%.4f-1=5.1\\    (%.2f)\\"%(dec,dec))

num1=12.123456
num2=12345678.4
print("%e"%num1)
print("%g"%num1,"%g"%num2)

print("小段to爸爸and妈妈：考卷做的不错,90%正确率,12%错误,满分102%,继续努力and保持。")

dis=1459787006
mS="The sun is{0:.5d}.".format(dis)

name="Ahg,Bgf,Cfe,Ded,Ecfe,Fagh,Gbgf,乱不乱？"
names=name.split(",")#print(names)
for name in names:
    print(name)
    
word=["My","name","is","Martin"]
long=" ".join(word)#print(long)

food="eggAndAppleAndbanana"#name.startswith("...")/endswith("...")

number="zxsudryenjxkcygrwnabcd    "
number.strip("abcd    ")

str1="HELLO"
str2="hello"
print(str1.lower(),str2.upper())
