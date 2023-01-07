# -*- coding: utf-8 -*-
"""Learn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uiipA_zXO3I4dtTYyF7OUe8umFaUNQQ4
"""

from google.colab import files
uploaded=files.upload()

import pandas as pd
import numpy as np
import datetime as dt
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

data=pd.read_csv('train.csv')
data=data.drop(['Product_id','Customer_name'],axis=1)
#data=data.replace({'Yes':1,'No ':0})
#data['instock_date'] = pd.to_datetime(data['instock_date']).map(dt.datetime.toordinal)
data=pd.get_dummies(data, prefix=['Cat'], columns=['Product_Category'])
data.head

y=np.array(data.iloc[:,-1])
x=np.array(data.iloc[:,:-1]).astype(float)
print(x)

imp = SimpleImputer(missing_values=np.nan, strategy='mean')
x = imp.fit_transform(x)
y = y.reshape(-1, 1)
y = imp.fit_transform(y)
y = y.reshape(-1)

lr=LinearRegression()
lr.fit(x,y)
pred=lr.predict(x)
print(pred)