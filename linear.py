# -*- coding: utf-8 -*-
#幼儿园分苹果，计算人数
# 7x=4(x+y)---->3x-4y=0
# 5y =2(x+y)+4----> -2x +3y =4
import numpy as np
a = np.array([[3,-4],[-2,3]])
b = np.array([0,4])
print (np.linalg.solve(a,b))
