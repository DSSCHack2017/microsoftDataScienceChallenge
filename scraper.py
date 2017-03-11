import requests
from bs4 import BeautifulSoup as bs


tickers = ['JP', 'KS', 'CH', 'HK', 'AAPL']


def get_news(link):
    base_link = "http://www.reuters.com/"
    link = base_link + link
    r = requests.get(link)

    article_soup = BeautifulSoup(r.content, 'html')

    article_span = soup.findAll('span', {'id': 'article-text'})

    paras = article_span[0].findAll('p')

    news = ' '.join(list(map(lambda k: k.getText(), paras)))

    return news

# date DDMMYYYY
def get_data_for_date(ticker, date):
    url = "http://www.reuters.com/finance/stocks/companyNews?symbol={}.O&date={}".format(ticker, date)
    r = requests.get(url)
    soup = BeautifulSoup(requests.get(url), 'html')
    links = soup.findAll('a')

    links_to_articles = list(map(lambda k: k[:8], links))

    day_news = ' '.join(list(map(lambda link: get_news(link), links_to_articles)))

    return day_news

def main():
