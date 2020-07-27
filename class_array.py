# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:07:12 2020

@author: duanyiting
"""
class array_operation:
    def _append_(List,something):
        List.append(something)
    def _getting_(List):
        for i in range(len(List)):
            print(List[i])
    def _sort_(List):
        List.sort()
    '''def _inverse_(List):
        for i in range(len(List)):
            for j in range(len(List)-1,0,-1):
                t=List[i]
                List[i]=List[j]
                List[j]=t
                print(i,j,List)'''