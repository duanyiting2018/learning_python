# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:48:26 2021

@author: duanyiting
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
from sklearn.tree import DecisionTreeRegressor as dtr
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dataset=pd.read_csv("Position_Salaries.csv")
X=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values
regressor=dtr(random_state=0)
regressor.fit(X,y)
y_pred=regressor.predict([[6.5]])
X_grid=np.arange(min(X),max(X),0.1)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color="green")
plt.plot(X_grid,regressor.predict(X_grid),color="red")
plt.title("决策树回归")
plt.xlabel("级别")
plt.ylabel("工资")
plt.show()
X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color="blue")
plt.plot(X_grid,regressor.predict(X_grid),color="green")
plt.title("支持向量回归")
plt.xlabel("级别")
plt.ylabel("工资")
plt.show()