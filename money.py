# -*- coding: utf-8 -*-
def money(fiveNumber,twoNumber,oneNumber):
    total=5*fiveNumber+2*twoNumber+oneNumber
    return total
fiveNumber=int(input("Enter a number of five:"))
twoNumber=int(input("Enter a number of two:"))
oneNumber=int(input("Enter a number of one:"))
print("total money is:",money(fiveNumber,twoNumber,oneNumber))