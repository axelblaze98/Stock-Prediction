# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 01:30:44 2020

@author: Parth Bhandari
"""

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from datetime import datetime
import pytz
from dateutil.tz import tzlocal
import csv

local = tzlocal()
now = datetime.now()
now = now.replace(tzinfo = local)

tz = pytz.timezone(r'America/New_York')
your_now = str(now.astimezone(tz))
y = your_now.split(' ');
date = y[0];
print(date);

stocks = ['AAPL','AMZN','F','FB','GOOG','IBM','INTC','MCD','MSFT','ORCL']

for i in stocks:
    url = 'https://in.finance.yahoo.com/quote/'+i+'?p='+i+'&.tsrc=fin-srch'
    uClient = uReq(url)
    page = uClient.read()
    uClient.close()
    page_soup = bs(page,'lxml')
    
    volume = page_soup.find('td',{'data-test':'TD_VOLUME-value'})
    close_price = page_soup.find('td',{'data-test':'PREV_CLOSE-value'})
    opening_price = page_soup.find('td',{'data-test':'OPEN-value'})
    bid_value = page_soup.find('td',{'data-test':'BID-value'})
    ask_value = page_soup.find('td',{'data-test':'ASK-value'})
    day_range = page_soup.find('td',{'data-test':'DAYS_RANGE-value'})
    x = day_range.text.split(' ')
    low = x[0];
    high = x[2];

    with open('./Dataset/'+i+'.csv','a',newline ='') as file:
        writer = csv.writer(file)
        writer.writerow([date,opening_price.text.replace(',',''),high.replace(',',''),low.replace(',',''),close_price.text.replace(',',''),'-',volume.text.replace(',','')])
    
