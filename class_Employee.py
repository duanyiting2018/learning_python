# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:20:48 2020

@author: duanyiting
"""

class Employee:
    def employee(no,name,money,money_plus):
        moneyplus=money/money_plus
        plus_money=money+moneyplus
        print(no,name,money,money_plus,moneyplus,plus_money)
Employee.employee(1977,"Jack",5400,30)  