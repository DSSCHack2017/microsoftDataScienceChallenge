from get_stock_data import *
import json
import pandas as pd
import datetime


# tickers = ['AAPL', 'MSFT', 'GOOG']
tickers = ['AAPL']
dates = pd.date_range('2012-01-01', '2012-12-31')
df = get_data(tickers, dates)
df = compute_daily_returns(df)
# dates = pd.date_range('2013-01-01', '2013-12-31')
# df = df.append(get_data(tickers, dates))
# dates = pd.date_range('2014-01-01', '2014-12-31')
# df = df.append(get_data(tickers, dates))
# dates = pd.date_range('2015-01-01', '2015-12-31')
# df = df.append(get_data(tickers, dates))
# dates = pd.date_range('2016-01-01', '2016-12-31')
# df = df.append(get_data(tickers, dates))

# df.to_csv("data/stock_prices.c")

with open('data/AAPL.json') as json_data:
    data = json.load(json_data)


def clean_date(date):
    mm = int(date[:2])
    dd = int(date[2:4])
    yy = int(date[4:])
    return datetime.date(yy, mm, dd)

cleaned_data = {}

for date, sentiment in data.items():
    cleaned_data[clean_date(date)] = sentiment


cd = pd.DataFrame.from_dict(cleaned_data, orient='index')
cd.columns = ['Polarity', 'Subjectivity']
# print(cd)
cd = df.join(cd)


print(cd)
