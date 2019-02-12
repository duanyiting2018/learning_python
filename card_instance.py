# -*- coding: utf-8 -*-
from card import Card
import random
deck=[]
hand=[]
for suit in range(1,5):
    for rank in range(1,14):
        deck.append(Card(rank,suit))
for i in range(5):
    a=random.choice(deck)
    hand.append(a)
    deck.remove(a)
print("\n")
print()
for card in hand:
    print(card.short_name,"=",card.long_name,"V:",card.value)