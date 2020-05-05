# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:06:51 2020

@author: duanyiting
"""
class Classification_1:
    def __init__(self):
        self.classification_name="分类1"
        self.classification_number=1514
    def classification_1(self):
        return self.classification_name+" "+str(self.classification_number)
    def classification_2(self,classification_2):
        return classification_2.classification_2()
    def __str__(self):
        return self.classification_name+" "+str(self.classification_number)
class Classification_2:
    def __init__(self):
        self.classification_name="分类2"
        self.classification_number=4273
    def classification_2(self):
        return self.classification_name+" "+str(self.classification_number)
    def __str__(self):
        return self.classification_name+" "+str(self.classification_number)
classification_1=Classification_1()
classification_2=Classification_2()
print(classification_1.classification_1())
print(classification_2.classification_2())#                |_=
print(classification_1.classification_2(classification_2))#|