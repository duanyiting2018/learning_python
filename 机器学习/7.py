# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:05:38 2021

@author: lenovo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
boston=datasets.load_boston()
print(boston.data.shape)
columns="crim zn indus chas nox rm age dis read tax ptratio b lstat".split()
x=pd.DataFrame(boston.data,columns=columns)
y=pd.DataFrame(boston.target)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
show_steps=True
included=[]
r2_list=[]
adjusted_r2_list=[]
best={"feature":"",
      "r2":"0",
      "adjusted_r2":0}
model=LinearRegression()
n=x_test.shape[0]
while True:
    changed=False
    if show_steps:
        print("")
    excluded=list(set(x.columns)-set(included))
    if show_steps:
            print("(步骤)排除的特征集=%s"%",".join(excluded))
    for new_column in excluded:
        if show_steps:
            print("(步骤)选择特征%s 特征集=%s"%(new_column,",".\
                join(included+[new_column])))
        fit=model.fit(x_train[included+[new_column]],y_train)
        r2=model.score(x_test[included+[new_column]],y_test)
        p=len(included)+1
        adjusted_r2=1-(((1-r2)*(n-1))/(n-p-1))
        if show_steps:
            print("(步骤)本次改进的拟合度：=%.3f;改进的拟合度的最大值=%.3f"%\
                  (adjusted_r2,best["adjusted_r2"]))
        if adjusted_r2>best["adjusted_r2"]:
            best={"feature":new_column,
                  "r2":r2,
                  "adjusted_r2":adjusted_r2}
            changed=True
            if show_steps:
                print("(步骤)更新改进的拟合度最大值：特征=%s;拟合度=%.3f;改进的拟合度=%.3f"%\
                  (best["feature"],best["r2"],best["adjusted_r2"]))
    if changed:
        r2_list.append(best["r2"])
        adjusted_r2_list.append(best["adjusted_r2"])
        included.append(best["feature"])
        excluded=list(set(excluded)-set(best["feature"]))
        print("增加特征 %-4s 拟合度=%.3f 改进的拟合度=%.3f"%(\
            best["feature"],best["r2"],best["adjusted_r2"]))
    else:
        break
print("")
print("最终选择的特征：")
print(", ".join(included))
x_range=len(np.array(r2_list))
plt.plot(range(1,x_range+1),r2_list,"--",label="拟合度")
plt.plot(range(1,x_range+1),adjusted_r2_list,"-",label="改进的拟合度")
plt.xlabel("特征数")
plt.legend()
plt.savefig("filename.png")
plt.show()