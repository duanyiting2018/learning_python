# -*- coding: utf-8 -*-
class Card:
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
        #rank
        if self.rank==1:
            self.rank="Ace"
            self.value=1
        elif self.rank==11:
            self.rank="Jack"
            self.value=10
        elif self.rank==12:
            self.rank="Queen"
            self.value=10
        elif self.rank==13:
            self.rank="King"
            self.value=10
        elif 2<=self.rank<=10:
            self.rank=str(self.rank)
            self.value=self.rank
        else:
            self.rank="RankError:suit max>13"
            self.value=-1
##################################################
#suit
##################################################
        if self.suit==1:
            self.suit="D"
        elif self.suit==2:
            self.suit="H"
        elif self.suit==3:
            self.suit="S"
        elif self.suit==4:
            self.suit="C"
        else:
            self.suit="SuitError:extra suit"
        self.short_name=self.rank[0]+self.suit[0]
        if self.rank=="10":
            self.short_name=self.rank+self.suit[0]
        self.long_name=self.rank+" of "+self.suit
        print("\n"+self.long_name,self.short_name)
#实例化请见代码card_instance.py