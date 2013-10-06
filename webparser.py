__author__ = 'michaellin'

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

    surprises =

    surprise_table = soup.find("table", {"class": "earningsurprise"})
    for row in surprise_table.findAll("tr"):

        cols = row.findAll("td")
        if len(cols) == 5:
            quarter = str(cols[0].getText())
            surprise = str(cols[4].getText())

            if quarter != "FiscalQuarter End":
                surprises[quarter] = surprise

    return surprises
