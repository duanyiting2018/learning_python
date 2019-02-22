# -*- coding: utf-8 -*-
class GameObject:
    def __init__(self,name):
        self.name=name
    def pickUp(self,player):
        print("This is prop(small).")
class Coin(GameObject):
    pass
my_coin=Coin("money")
my_coin.pickUp("boy/girl")
class Bubble_gum(GameObject):
    def pickUp(self):
        print("This is prop(big).")
my_Bubble_gum=Bubble_gum("bubble")
my_Bubble_gum.pickUp()