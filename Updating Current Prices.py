# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:15:09 2020

@author: Parth Bhandari
"""
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import numpy as np

stocks = ['AAPL','AMZN','F','FB','GOOG','IBM','INTC','MCD','MSFT','ORCL']

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

for i in stocks:
    
    url = 'https://in.finance.yahoo.com/quote/'+i+'?p'+i+'&.tsrc=fin-srch'
    uClient = uReq(url)
    webpage = uClient.read()
    uClient.close()

    page_soup = bs(webpage,"html.parser")
    value = page_soup.find('span',{"class":"Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"})
    cur_price = value.text.replace(',','')
    
    mycursor = conn.cursor()
    mycursor.execute("use major1db;")
    mycursor.execute("update stock_predicted set cur_price = %s where stk_name = %s;",(float(cur_price),i))
    conn.commit()

mycursor.execute("select * from stock_predicted")
   
for i in mycursor:
    print(i)
