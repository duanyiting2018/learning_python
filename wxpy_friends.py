# -*- coding: utf-8 -*-
import wxpy
bot=wxpy.Bot()
my_friends=bot.friends()
male=0
female=0
other=0
for friend in my_friends:
    if friend.sex==1:
        male+=1
    if friend.sex==2:
        female+=1
    if friend.sex==0:
        other+=1
print("male=",male)
print("female=",female)
print("other=",other)
print("total number is",len(my_friends))