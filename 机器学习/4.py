# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 09:28:05 2021

@author: duanyiting
"""
#支持向量回归 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer,OneHotEncoder
from sklearn.preprocessing import LabelEncoder as le
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler as ss
from sklearn.linear_model import LinearRegression as lr
from sklearn.preprocessing import PolynomialFeatures as pf
from sklearn.svm import SVR
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dataset=pd.read_csv("Position_Salaries.csv")
X=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2:3].values
sc_X=ss()
sc_y=ss()
X=sc_X.fit_transform(X)
y=sc_y.fit_transform(y)
regressor=SVR(kernel="rbf")
regressor.fit(X,y)
y_pred=regressor.predict([[6.5]])
y_pred=sc_y.inverse_transform(y_pred)

plt.scatter(X,y,color="blue")
plt.plot(X,regressor.predict(X),color="green")
plt.title("支持向量回归")
plt.xlabel("级别")
plt.ylabel("工资")
plt.show()
X_grid=np.arange(min(X),max(X),0.01)
x_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color="blue")
plt.plot(X_grid,regressor.predict(X_grid),color="green")
plt.title("支持向量回归")
plt.xlabel("级别")
plt.ylabel("工资")
plt.show()