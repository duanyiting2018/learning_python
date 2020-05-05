# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:11:26 2020

@author: duanyiting
"""
class Classification_1:
    def __init__(self):
        self.classification_type="鞋子"
        self.classification_number=7263
    def classification_1(self):
        return self.classification_type+" "+str(self.classification_number)
    def classification_2(self,classification_2):
        return classification_2.classification_2()
    def Classification_3(self,classification_3):
        return classification_3.Classification_3()
    def __str__(self):
        return self.classification_type+" "+str(self.classification_number)
class Classification_2:
    def __init__(self):
        self.classification_name="张三"
        self.classification_age=36
    def classification_2(self):
        return self.classification_name+" "+str(self.classification_age)
    def __str__(self):
        return self.classification_name+" "+str(self.classification_age)
class Classification_3:
    def __init__(self):
        self.Classification_name="跑鞋1"
        self.Classification_money=382
    def Classification_3(self):
        return self.Classification_name+" "+str(self.Classification_money)
    def __str__(self):
        return self.Classification_name+" "+str(self.Classification_money)
classification_1=Classification_1()
classification_2=Classification_2()
classification_3=Classification_3()
print(classification_1.classification_1())
print(classification_2.classification_2())
print(classification_3.Classification_3())
print(classification_1.classification_2(classification_2))
print(classification_1.Classification_3(classification_3))