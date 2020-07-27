# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:37:40 2020

@author: duanyiting
"""
class employee:
    #__init__==setting
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    #__str__==getting
    def __str__(self):
        return "name:"+self.name+"\t age:"+str(self.age)+"\t sex:"+self.sex
class employee1(employee):
    def __init__(self,name,age,sex,level,salary1):
        super().__init__(name,age,sex)
        self.level=level
        self.salary1=salary1
    def __str__(self):
        return "name:"+self.name+"\t age:"+str(self.age)+"\t sex:"+self.sex+ \
    "level:"+self.level+"salary1:"+str(self.salary1)
class employee2(employee):
    def __init__(self,name,age,sex,depart,salary2):
        super().__init__(name,age,sex)
        self.depart=depart
        self.salary2=salary2
    def __str__(self):
        return "name:"+self.name+" \t age:"+str(self.age)+"\t sex:"+self.sex+ \
    "\n depart:"+self.depart+"\t salary2:"+str(self.salary2)
employee1=employee1("老八",22,"男","3级",300000)
employee2=employee2("老八秘制小汉堡",21,"生物","生物部",10000)
print(employee1)
print(employee2)
        
'''employee-------------------
    |                        |
    |                        |
 employee1               employee2'''