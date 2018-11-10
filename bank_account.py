# -*- coding: utf-8 -*-
class Alipay_account:
    def __init__(self,sth,account,cash):
        self.sth=sth
        self.account=account
        self.cash=cash
    def read(self):
        print(self.cash)
        return self.cash
    def deposit(self,money):
        self.cash+=money
    def withdraw(self,money2):
        self.cash-=money2
    def __str__(self):
        return self.sth+" "+self.account+" "+str(self.cash)
my_account=Alipay_account("dyt","183742538",100)
my_account.deposit(8)
my_account.withdraw(5)
my_account.read()
print(my_account)
class Alipay_account2(Alipay_account):
    def __init__(self,sth,account,cash,interest):
        Alipay_account.__init__(sth,account,cash)
        self.interest=interest