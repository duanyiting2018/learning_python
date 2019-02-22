# -*- coding: utf-8 -*-
class hotdog:
    def __init__(self):
        self.cook_level=0
        self.cook_string="0分熟"
        self.condiments=[hotdog]
    def cook(self,time):
        self.cook_level+=time
        if self.cook_level>6:
            self.cook_string="7~10分熟"
        elif self.cook_level>=1:
            self.cook_string="1~6分熟"
        elif self.cook_level>0:
            self.cook_string=">0分熟"
    def __str__(self):
        return str(self.cook_level)+" "+self.cook_string
my_hotdog=hotdog()
my_hotdog.cook(8)
print(my_hotdog)
your_hotdog=hotdog()
your_hotdog.cook(5)
print(your_hotdog)