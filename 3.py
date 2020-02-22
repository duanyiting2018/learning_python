# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:59:11 2020

@author: duanyiting
"""
times=[]
for i in range(0,7):
    line=list(map(int, input().split()))
    times.append(line[0])
    times.append(line[1])
day1=times[0]+times[1]
day2=times[2]+times[3]
day3=times[4]+times[5]
day4=times[6]+times[7]
day5=times[8]+times[9]
day6=times[10]+times[11]
day7=times[12]+times[13]
merge=[]
merge.extend([day1,day2,day3,day4,day5,day6,day7])
times2=merge[:]
merge.sort()
print(times2.index(merge[6])+1)