# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:41:23 2020

@author: duanyiting
"""
#多项式回归 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer,OneHotEncoder
from sklearn.preprocessing import LabelEncoder as le
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler as ss
from sklearn.linear_model import LinearRegression as lr
from sklearn.preprocessing import PolynomialFeatures as pf
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dataset=pd.read_csv("Position_Salaries.csv")
X=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values
lin_reg=lr()
lin_reg.fit(X,y)
poly_reg=pf(degree=4)
X_poly=poly_reg.fit_transform(X)
poly_reg.fit(X_poly,y)
lin_reg2=lr()
lin_reg2.fit(X_poly,y)
plt.scatter(X,y,color="green")
plt.plot(X,lin_reg.predict(X),color="blue")
plt.title("线性回归")
plt.xlabel("级别")
plt.ylabel("工资")
plt.show()
plt.scatter(X,y,color="green")
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), \
         color="blue")
plt.title("多项式回归（参数为4）")
plt.xlabel("级别")
plt.ylabel("工资")
plt.show()
X_grid=np.arange(min(X),max(X),0.1)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color="red")
plt.plot(X_grid,lin_reg2.predict(poly_reg. \
                                 fit_transform(X_grid)),color="green")
plt.title("多项式回归（参数为5）")
plt.xlabel("级别")
plt.ylabel("工资")
plt.show()
print(lin_reg.predict(np.array([[6.5]])))
print(lin_reg2.predict(poly_reg.fit_transform(np.array([[6.5]]))))
