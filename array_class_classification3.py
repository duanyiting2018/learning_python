# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:27:06 2020

@author: duanyiting
"""
class Classification_1:
    def __init__(self):
        self.classification_name="李四1"
        self.classification_role="角色名1"
    def Classification_1(self):
        return self.classification_name+" "+self.classification_role
    def Classification_3(self,classification_3):
        return classification_3.Classification_3()
    def Classification_4(self,classification_4):
        return classification_4.Classification_4()
    def __str__(self):
        return self.classification_name+" "+self.classification_role
class Classification_2:
    def __init__(self):
        self.classification_permission="权限1"
    def Classification_2(self):
        return self.classification_permission
    def Classification_1(self):
        return self.classification_permission
    def Classification_3(self,classification_3):
        return classification_3.Classification_3()
    def __str__(self):
        return self.classification_permission
class Classification_3:
    def __init__(self):
        self.classification_name="角色名2"
        self.Classification_type="角色2"
    def Classification_3(self):
        return self.classification_name+" "+self.Classification_type
    def __str__(self):
        return self.classification_name+" "+self.Classification_type
class Classification_4:
    def __init__(self):
        self.classification_name="李四2"
    def Classification_4(self):
        return self.classification_name
    def __str__(self):
        return self.classification_name
classification_1=Classification_1()
classification_2=Classification_2()
classification_3=Classification_3()
classification_4=Classification_4()
print(classification_1.Classification_1())
print(classification_2.Classification_2())
print(classification_3.Classification_3())
print(classification_4.Classification_4())
print(classification_1.Classification_3(classification_3))
print(classification_1.Classification_4(classification_4))
print(classification_2.Classification_3(classification_3))