# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:15:09 2020

@author: Parth Bhandari
"""
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import numpy as np
import threading
from datetime import datetime, time
import pytz
import pymysql

stocks = ['AAPL','AMZN','F','FB','GOOG','IBM','INTC','MCD','MSFT','ORCL']
    
pymysql.converters.encoders[np.float64] = pymysql.converters.escape_float
pymysql.converters.conversions = pymysql.converters.encoders.copy()
pymysql.converters.conversions.update(pymysql.converters.decoders)
    
host = '#####'
port = 3306
dbname = 'major1db'
user = '#####'
password = '#####'

end_time = time(16, 00)

def timeUP(time_now):
    if time_now > end_time:
        return False
    else:
        return True
    
def run_check():
    time_now = datetime.now(pytz.timezone('America/New_York')).time()
    if timeUP(time_now):
        print(time_now)
        threading.Timer(240.0,run_check).start()
        print(time_now)
        conn = pymysql.connect(host, user=user,port=port,passwd=password, db=dbname)
        mycursor = conn.cursor()
        for i in stocks:
            url = 'https://in.finance.yahoo.com/quote/'+i+'?p'+i+'&.tsrc=fin-srch'
            uClient = uReq(url)
            webpage = uClient.read()
            uClient.close()

            page_soup = bs(webpage,"lxml")
            cur_price = page_soup.find('span',{"class":"Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"})
            volume = page_soup.find('td',{'data-test':'TD_VOLUME-value'})
            day_range = page_soup.find('td',{'data-test':'DAYS_RANGE-value'})
            x = day_range.text.split(' ')
            low = x[0];
            high = x[2];
    
            mycursor = conn.cursor()
            mycursor.execute("use major1db;")
            mycursor.execute("update stock_predicted set cur_price = %s where stk_name = %s;",(float(cur_price.text.replace(',','')),i))
            mycursor.execute("update market set volume = %s where stk_name = %s;",(int(volume.text.replace(',','')),i))
            mycursor.execute("update market set high = %s where stk_name = %s;",(float(high.replace(',','')),i))
            mycursor.execute("update market set low = %s where stk_name = %s;",(float(low.replace(',','')),i))
            conn.commit()

        conn.close()
        
run_check()