import numpy as np
import pandas as pd
import yfinance as yf

class Data:
    def __init__(self, universe):
        self.universe = universe
        self.tickers = self.get_tickers()
        self.data = self.get_raw_data()

    def get_tickers(self):
        return pd.read_excel('tickers.xlsx', header=None).iloc[:,0].values

    def get_raw_data(self):
        return yf.download(' '.join(self.tickers), period='max')

    def get_returns(self, start='2010-01-01', end='2021-04-01'):
        prices = self.data['Adj Close'].loc[start:end]
        return (prices.diff(1)/prices.shift(1)).dropna(axis=0, how='all')

    def get_volume(self, start='2010-01-01', end='2021-04-01'):
        return self.data['Volume'].loc[start:end]
