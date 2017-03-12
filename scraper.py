import requests
from bs4 import BeautifulSoup
from datetime import timedelta, date


# tickers = ['JP', 'KS', 'CH', 'HK', 'AAPL']
# tickers = ['AAPL']
tickers = ['JP', 'KS', 'CH', 'HK']

def get_news(link):
    base_link = "http://www.reuters.com/"
    link = base_link + link

    r = requests.get(link)
    article_soup = BeautifulSoup(r.content, 'html')

    article_span = article_soup.findAll('span', {'id': 'article-text'})
    paras = article_span[0].findAll('p')
    news = ' '.join(list(map(lambda k: k.getText(), paras)))

    return news


# date MMDDYYYY
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
    print("Links to articles", links_to_articles)
    day_news = ' '.join(list(map(lambda link: get_news(link['href']), links_to_articles)))
    if day_news:
        print(day_news)
    return day_news


def get_sentiment_of_news(news):
    return 1


def main():

    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    sentiments = {}
    # start_date = date(2007, 1, 4)
    # end_date = date(2016, 12, 31)
    start_date = date(2013, 9, 9)
    end_date = date(2013, 9, 11)
    for ticker in tickers:
        sentiments[ticker] = {}
        for single_date in daterange(start_date, end_date):
            str_date = single_date.strftime("%m%d%Y")
            print(str_date)
            sentiments[ticker][str(single_date)] = get_sentiment_for_date(ticker, str_date)
    print(sentiments)

main()
