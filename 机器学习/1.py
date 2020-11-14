# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def show(boolean):
    if boolean==0:
        print(X,y)
    elif boolean==1:
        print(X_tr,"|",X_te,"|",y_tr,"|",y_te)
    elif boolean==2:
        pass

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer,OneHotEncoder
from sklearn.preprocessing import LabelEncoder as le
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler as ss

#打印表格 
'''
Country	Age	Salary	Purchased
France	44	72000	No
Spain	27	48000	Yes
Germany	30	54000	No
Spain	38	61000	No
Germany	40		    Yes
France	35	58000	Yes
Spain		52000	No
France	48	79000	Yes
Germany	50	83000	No
France	37	67000	Yes
'''
dataset=pd.read_csv("data_bak.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values
#show(0)

#补充缺失数据 
imputer=Imputer(missing_values="NaN",strategy="mean", \
                axis=0,verbose=0,copy=True)
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
#show(0)

#给数据打上标签 
le_y=le()
y=le_y.fit_transform(y)
le_X=le()
X[:,0]=le_X.fit_transform(X[:,0])
#show(0)

#哑变量编码 
enc=OneHotEncoder(categorical_features=[0])
X=enc.fit_transform(X).toarray()
#show(0)

#划分训练集和测试集 
X_tr,X_te,y_tr,y_te=tts(X,y,test_size=0.3,random_state=0)
show(1)

#特征缩放 
ss=ss()
X_tr=ss.fit_transform(X_tr)
X_te=ss.transform(X_te)