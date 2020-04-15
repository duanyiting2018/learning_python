# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:12:07 2020

@author: duanyiting
"""
class account:
    #def __init__(self):
        #self.account_name=input()
        #self.account_money=int(input())
    def see_account(self):
        print(self.account_name,",",self.account_money)
    def change_account(self):
        name=input()
        money=int(input())
        self.account_name=name
        self.account_money=money
account=account()
account.change_account()
account.see_account()