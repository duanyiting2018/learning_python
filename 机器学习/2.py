# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:57:42 2020

@author: duanyiting
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer,OneHotEncoder
from sklearn.preprocessing import LabelEncoder as le
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler as ss
from sklearn.linear_model import LinearRegression as lr
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#简单线性回归 
'''dataset=pd.read_csv("Salary_Data.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
X_tr,X_te,y_tr,y_te=tts(X,y,test_size=1/3,random_state=0)
sc_X=ss()
X_tr=sc_X.fit_transform(X_tr)
X_te=sc_X.transform(X_te)
sc_y=ss()
y_tr=sc_y.fit_transform(y_tr)
regressor=lr()
regressor.fit(X_tr,y_tr)
y_pred=regressor.predict(X_te)
plt.scatter(X_tr,y_tr,color="green")
plt.plot(X_tr,regressor.predict(X_tr),color="red")
plt.title("工资及年限(训练)")
plt.xlabel("工作年限/年")
plt.ylabel("工资")
plt.show()
plt.scatter(X_tr,y_tr,color="green")
plt.plot(X_tr,regressor.predict(X_tr),color="red")
plt.title("工资及年限(测试)")
plt.xlabel("工作年限/年")
plt.ylabel("工资")
plt.show()'''
#多元线性回归 
dataset=pd.read_csv("50_Startups.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
le=le()
X[:,3]=le.fit_transform(X[:,3])
onehotencoder=OneHotEncoder(categorical_features=[3])
X=onehotencoder.fit_transform(X).toarray()
X=X[:,1:]
X_tr,X_te,y_tr,y_te=tts(X,y,test_size=0.3,random_state=0)
regressor=lr()
regressor.fit(X_tr,y_tr)
y_pred=regressor.predict(X_te)