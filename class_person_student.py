# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:age3:33 2020

@author: duanyiting
"""
class Person:
    def __init__(self,name,addr,sex,age):
        self.name=name
        self.addr=addr
        self.sex=sex
        self.age=age
    def output1(self,name,addr,sex,age):
        print("name:",name,"addr:",addr,"sex:",sex,"age:",age)
    def output2(self,name,sex,age):
        print("name:",name,"sex:",sex,"age:",age)
    def output3(self,age):
        print("age:",age)
class Student(Person):
    def __init__(self,math,english):
        self.math=math
        self.english=english
    def output1(self,name,addr,sex,age,math,english):
        print("name:",name,"addr:",addr,"sex:",sex,"age:",age,"math:"\
              ,str(math),"english",str(english))
    def output2(self,addr,sex,age,english):
        print("addr:",addr,"sex:",sex,"age:",age,"english",str(english))
    def output3(self,math):
        print("math:",str(math))
person=Person("1","2","3",4)
student=Student(5,6)
name,addr,sex,age,math,english="1","2","3",4,5,6
person.output1(name,addr,sex,age)
person.output2(name,sex,age)
person.output3(age)
student.output1(name,addr,sex,age,math,english)
student.output2(addr,sex,age,english)
student.output3(math)
#也可以不用输入参数,可以调用内部参数( \
#就是把参数(除self以外)都去掉,print()里面输出的参数都加self.xxx( \
#可以参考class_employee2.py))
#记得把123456改成对应的属性哦~ 