from get_stock_data import *


tickers = ['AAPL', 'MSFT', 'GOOG']
dates = pd.date_range('2012-01-01', '2012-12-31')
df = get_data(tickers, dates)
dates = pd.date_range('2013-01-01', '2013-12-31')
df = df.append(get_data(tickers, dates))
dates = pd.date_range('2014-01-01', '2014-12-31')
df = df.append(get_data(tickers, dates))
dates = pd.date_range('2015-01-01', '2015-12-31')
df = df.append(get_data(tickers, dates))
dates = pd.date_range('2016-01-01', '2016-12-31')
df = df.append(get_data(tickers, dates))

df.to_csv("data/stock_prices.c")

print(df)
