# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 11:38:02 2021

@author: lenovo
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''from sklearn.preprocessing import Imputer,OneHotEncoder
from sklearn.preprocessing import LabelEncoder as le
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler as ss
from sklearn.linear_model import LinearRegression as lr
from sklearn.preprocessing import PolynomialFeatures as pf'''
from sklearn.ensemble import RandomForestRegressor as rfr
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dataset=pd.read_csv("Position_Salaries.csv")
regressor=rfr(n_estimators=100,random_state=0)
X=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values
regressor.fit(X,y)
y_pred=regressor.predict([[6.5]])
X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color="red")
plt.plot(X_grid,regressor.predict(X_grid),color="green")
plt.title("随机森林回归")
plt.xlabel("级别")
plt.ylabel("工资")
plt.show()