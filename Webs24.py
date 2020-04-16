# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 02:17:03 2020

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

    page_soup = bs(webpage,"lxml")
    close_price = page_soup.find('td',{'data-test':'PREV_CLOSE-value'})
    opening_price = page_soup.find('td',{'data-test':'OPEN-value'})
    bid_value = page_soup.find('td',{'data-test':'BID-value'})
    ask_value = page_soup.find('td',{'data-test':'ASK-value'})
    
    mycursor = conn.cursor()
    mycursor.execute("use major1db;")
    mycursor.execute("update market set close_price = %s where stk_name = %s;",(float(close_price.text.replace(',','')),i))
    mycursor.execute("update market set open_price = %s where stk_name = %s;",(float(opening_price.text.replace(',','')),i))
    mycursor.execute("update market set ask = %s where stk_name = %s;",(ask_value.text,i))
    mycursor.execute("update market set bid = %s where stk_name = %s;",(bid_value.text,i))
    conn.commit()
    
conn.close()