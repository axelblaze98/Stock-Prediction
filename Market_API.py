# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:18:51 2020

@author: Parth Bhandari
"""

from flask import jsonify
import flask
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = flask.Flask(__name__)

@app.route('/',methods =['GET'])
def main():
    market = []
    stocks = ['AAPL','AMZN','F','FB','GOOG','IBM','INTC','MCD','MSFT','ORCL']
    a=1
    for i in stocks:
        url = 'https://in.finance.yahoo.com/quote/'+i+'?p'+i+'&.tsrc=fin-srch'
        uClient = uReq(url)
        webpage = uClient.read()
        uClient.close()
    
        page_soup = bs(webpage,"lxml")
        volume = page_soup.find('td',{'data-test':'TD_VOLUME-value'})
        day_range = page_soup.find('td',{'data-test':'DAYS_RANGE-value'})
        x = day_range.text.split(' ')
        low = x[0];
        high = x[2];
        close_price = page_soup.find('td',{'data-test':'PREV_CLOSE-value'})
        open_price = page_soup.find('td',{'data-test':'OPEN-value'})
        bid_value = page_soup.find('td',{'data-test':'BID-value'})
        ask_value = page_soup.find('td',{'data-test':'ASK-value'})
    
        value = {'stkid' : a,
                 'stk_name' : i, 
                 'volume' : volume.text.replace(',',''),
                 'low' : low.replace(',',''),
                 'high' : high.replace(',',''),
                 'open_price' : open_price.text.replace(',',''),
                 'close_price' : close_price.text.replace(',',''),
                 'bid': bid_value.text.replace(',',''),
                 'ask' : ask_value.text.replace(',','')}
        market.append(value)
        a=a+1
    
    return jsonify(market)

if __name__=='__main__':
    app.run(host="localhost",port = 5000)