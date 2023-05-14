import pandas as pd
from prophet import Prophet
import DataLoader as dl

code = '92102'
def predict(code):
    price_df = dl.korea_stock(code, '2020-01-01','2023-04-16')
    
    price_df['y'] = price_df['Close']
    price_df['ds'] = price_df.index
    
    
    df = price_df[['ds','y']]
    
    m = Prophet()
    m.fit(df)
    
    future = m.make_future_dataframe(periods=30)
    future.tail()
    
    forecast = m.predict(future)
    figl = m.plot(forecast)
    return forecast