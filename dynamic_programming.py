# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:19:44 2020

@author: duanyiting
"""
num=[1,4,3,4,2,3]
def dynamic_programming(nums):
    dp=[]
    #dp数组全部初始化为 1 
    for i in range(0,len(nums)):
        dp.append(1)
    for i in range(0,len(nums)):
        for j in range(1,i):
            if nums[i]>nums[j]:
                dp[i]=max(dp[i],dp[j]+1)
    res=0
    for i in range(0,len(dp)):
        res=max(res,dp[i])
    return res
print(dynamic_programming(num))