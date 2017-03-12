from get_stock_data import *
import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime


# tickers = ['AAPL', 'MSFT', 'GOOG']
# df.to_csv("data/stock_prices.c")

def clean_date(date):
    mm = int(date[:2])
    dd = int(date[2:4])
    yy = int(date[4:])
    return datetime.date(yy, mm, dd)

def create_df_for_ticker(ticker):
    tickers = [ticker]
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

    df = compute_daily_returns(df)

    with open('data/{}.json'.format(ticker)) as json_data:
        data = json.load(json_data)

    cleaned_data = {}

    for date, sentiment in data.items():
        cleaned_data[clean_date(date)] = sentiment

    cd = pd.DataFrame.from_dict(cleaned_data, orient='index')
    cd.columns = ['Polarity', 'Subjectivity']
    cd = df.join(cd)
    cd = cd.drop('SPY', 1)

    return cd

msft = create_df_for_ticker('MSFT')
msft = msft.fillna(method='backfill')

msft.to_csv("data/msft_complete.csv")
# # Initialize the model class.
# model = LinearRegression()
# # Fit the model to the training data.
# model.fit(list(map(lambda k: [k], aapl['Polarity'].tolist())), list(map(lambda k: [k], aapl['AAPL'].tolist())))
#
# print("fitting complete")
# print(model.coef_)
# print(model.predict(0.4))

# ax = aapl[:100].plot()
# plt.show()
# goog = create_df_for_ticker('GOOG')
# msft = create_df_for_ticker('MSFT')

# print(aapl)
# print(goog)
# print(msft)
