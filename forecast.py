# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine
from prophet import Prophet
import DataLoader as dl
import pandas_datareader.data as web


def forecast(code, start='2020-01-01',end=None,period=30):
    price_df = dl.korea_stock(code, '2020-01-01','2023-04-16')
    
    price_df['y'] = price_df['Close']
    price_df['ds'] = price_df.index
    
    
    df = price_df[['ds','y']]
    
    m = Prophet()
    m.fit(df)
    
    future = m.make_future_dataframe(periods=30)
    future.tail()
    
    forecast = m.predict(future)
    fig = m.plot(forecast)
    return fig