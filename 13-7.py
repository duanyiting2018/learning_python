# -*- coding: utf-8 -*-
def calculateTax(price,tax_rate):
    total=price+(price*tax_rate)
    my_price=10000
    print("my_price=",my_price)
    return total
my_price=float(input("Enter a price:"))
totalPrice=calculateTax(my_price,0.06)
print("price=",my_price,"total price=",totalPrice)
print("my_price=",my_price)