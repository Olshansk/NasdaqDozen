__author__ = 'linmichaelj'

import urllib2
from bs4 import BeautifulSoup
#requires html5lib

def get_soup(url):
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    return BeautifulSoup(data, "html5lib")


def get_recommendation(symbol):
    soup = get_soup("http://ca.finance.yahoo.com/q/ao?s=" + symbol)
    data_tables = soup.findAll("table", {"class": "yfnc_datamodoutline1"})

    #Look at Recommendation Summary
    mean_recommendation = str(data_tables[0].find("td", {"class": "yfnc_tabledata1"}).getText())

    recommendations = {}

    #Look at Recommendation Trends Table
    for row in data_tables[3].find("tr").findAll("tr"):
        recommendation = row.find("th", {"align": "left"})
        if recommendation is not None:
            recommendation = recommendation.getText()
            num = row.find("td", {"class": "yfnc_tabledata1"}).getText()

            #add to database, str is used to convert from unicode to string
            recommendations[str(recommendation)] = str(num)

    return mean_recommendation, recommendations


def get_quart_earning_surprise(symbol):
    soup = get_soup("http://www.nasdaq.com/symbol/" + symbol + "/earnings-surprise")

    surprises = {}

    surprise_table = soup.find("table", {"class": "earningsurprise"})
    for row in surprise_table.findAll("tr"):

        cols = row.findAll("td")
        if len(cols) == 5:
            quarter = str(cols[0].getText())
            surprise = str(cols[4].getText())

            if quarter != "FiscalQuarter End":
                surprises[quarter] = surprise

    return surprises


def get_eps_forecast(symbol):
    soup = get_soup("http://www.nasdaq.com/symbol/" + symbol + "/earnings-forecast")

    forecasts = {}

    forecast_table = soup.find("table", {"class": "earningsurprise"})
    rows = forecast_table.findAll("tr")
    for i in range(1, len(rows)):
        cols = rows[i].findAll("td")
        year = cols[0].getText()
        year = year[len(year)-4:]
        forecast = cols[1].getText()
        forecasts[str(year)] = str(forecast)

    return forecasts


def get_industry_pe(symbol):
    soup = "http://finance.yahoo.com/q/in?s=" + symbol + "+Industry"

    industry_table = soup.find("table", {"class": "yfnc_datamodoutline1"})
    industry_url = industry_table.
