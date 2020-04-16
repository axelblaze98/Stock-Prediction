# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 02:09:52 2019

@author: Parth Bhandari
"""

import pandas as pd
import joblib
import numpy as np

list1 = ['AAPL.csv','AMZN.csv','F.csv','FB.csv','GOOG.csv','IBM.csv','INTC.csv','MCD.csv','MSFT.csv','ORCL.csv']
list2 = ['apple.pkl', 'amazon.pkl', 'ford.pkl', 'facebook.pkl', 'google.pkl', 'IBM.pkl', 'intel.pkl', 'mcd.pkl', 'microsoft.pkl', 'orcl.pkl']

import pymysql
    
pymysql.converters.encoders[np.float64] = pymysql.converters.escape_float
pymysql.converters.conversions = pymysql.converters.encoders.copy()
pymysql.converters.conversions.update(pymysql.converters.decoders)
    
host = '#####'
port = 3306
dbname = 'major1db'
user = '#####'
password = '#####'
    
conn = pymysql.connect(host, user=user,port=port,passwd=password, db=dbname)
mycursor = conn.cursor()
    
    
for _ in range(len(list1)):
    
    datasets = "./Dataset/"+list1[_]
    df = pd.read_csv(datasets,na_values=['null'],index_col='Date',parse_dates=True,infer_datetime_format=True)
    feature_columns = ['High', 'Low', 'Close']
    
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    feature_minmax_transform_data = scaler.fit_transform(df[feature_columns])
    feature_minmax_transform = pd.DataFrame(columns=feature_columns, data=feature_minmax_transform_data, index=df.index)
    
    models = "./Models/"+list2[_]
    model = joblib.load(models)
     
    test = np.array(feature_minmax_transform[-1:])
    test = test.reshape(1,1,3)
    y = model.predict(test)
    y = float(y)
    
    mycursor = conn.cursor()
    mycursor.execute("use major1db;")
    mycursor.execute("update stock_predicted set pr_price = %s where stkid = %s;",(y, _+1))
    conn.commit()

conn.close()