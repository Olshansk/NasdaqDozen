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
    mean_recommendation = data_tables[0].find("td", {"class": "yfnc_tabledata1"}).getText()

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


def 