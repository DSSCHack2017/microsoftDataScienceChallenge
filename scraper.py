import requests
from bs4 import BeautifulSoup as bs

url = "https://www.bloomberg.com/markets/earnings-calendar/us"

def get_data_for_date(ticker, date):
    
