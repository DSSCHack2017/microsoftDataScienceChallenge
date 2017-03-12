import requests
from bs4 import BeautifulSoup
import threading
from datetime import timedelta, date
# from textblob import TextBlob
import json


# tickers = ['AAPL', 'MSFT', 'GOOG']
tickers = ['AAPL']


def get_news(link):
    base_link = "http://www.reuters.com/"
    link = base_link + link

    r = requests.get(link)
    article_soup = BeautifulSoup(r.content, 'html')

    article_span = article_soup.findAll('span', {'id': 'article-text'})
    paras = article_span[0].findAll('p')
    news = ' '.join(list(map(lambda k: k.getText(), paras)))

    return news


def get_sentiment_for_date(ticker, date):
    """
    Args
        :ticker stock symbol
        :date mmddyy as string
    Return
        :int sentiment of the news for the day for the stock
    """
    url = "http://www.reuters.com/finance/stocks/companyNews?symbol={}&date={}".format(ticker, date)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html')
    links = soup.findAll('a')
    links_to_articles = []
    for link in links:
        if link['href'][:8] == "/article":
            links_to_articles.append(link)
    day_news = ' '.join(list(map(lambda link: get_news(link['href']), links_to_articles)))
    if day_news:
        print(day_news)
        return get_sentiment_of_news(day_news)
    else:
        print("No news found")


def get_sentiment_of_news(news):
    return 1
    # sent = TextBlob(news)
    # return [sent.sentiment.polarity, sent.sentiment.subjectivity]


def main():
    for ticker in tickers:
        if ticker == "AAPL":
            sentiment = get_sentiment_for_date(ticker, "03092017")
        # prediction = azure_predict(ticker, sentiment)
        # print(ticker, prediction)


main()
