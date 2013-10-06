__author__ = 'michaellin'

import ystockquote
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime as dt
import json

def sortStocks(stocks,  stat):
    d = {}
    for stock in stocks:
        d[ystockquote._request(stock, stat)] = stock

    sortedKeys = d.keys()
    sortedKeys.sort()

    for key in sortedKeys:
        print(d[key] + ", " + key)

def graphHistorical(symbol, attribute, startDate, endDate):
    x = []
    y = []
    j = ystockquote.get_historical_prices(symbol, startDate, endDate)
    for key in j.keys():
        some_time_dt = dt.datetime.strptime(key, '%Y-%m-%d')
        some_time_num = mpl.dates.date2num(some_time_dt) # 734126.20833333337
        x.append(some_time_dt)
        y.append(j[key][attribute])

    plt.plot_date(x, y)
    plt.ylabel(attribute)
    plt.xlabel("date")
    plt.show()
