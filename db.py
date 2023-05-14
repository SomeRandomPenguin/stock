# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine
from prophet import Prophet
import DataLoader as dl
import pandas_datareader.data as web
import pandas as pd

con = create_engine('mysql+pymysql://root:django@34.210.26.166:58936/stock')

def info1(code):
    query = f'''
            select * from stock.info
            where 종목코드 = '{code}';
            '''
    print(query)
    df = pd.read_sql(query, con)
    return df

def info2(code):
    query = f'''
            select * from stock.info
            where 회사명 = '{code}';
            '''
    print(query)
    df = pd.read_sql(query, con)
    return df
# 업종, 주요제품, 대표자명, 홈페이지 
def name():
    query = f'''
            select 회사명, 종목코드 from stock.info;
            '''
    print(query)
    df = pd.read_sql(query, con)
    return df['회사명'] + ' - ' + df['종목코드']

# def forecast(code, start='2020-01-01',end=None,period=30):
#     price_df = dl.korea_stock(code, '2020-01-01','2023-04-16')
    
#     price_df['y'] = price_df['Close']
#     price_df['ds'] = price_df.index
    
    
#     df = price_df[['ds','y']]
    
#     m = Prophet()
#     m.fit(df)
    
#     future = m.make_future_dataframe(periods=30)
#     future.tail()
    
#     forecast = m.predict(future)
#     fig = m.plot(forecast)
#     return fig

def korea_stock(code, start, end=None):
    df = pd.DataFrame()
    if end is None:
        df = web.DataReader(code, 'naver', start=start)
    else:
        df = web.DataReader(code, 'naver', start=start,end=end)
    df = df.astype('int')
    return df

def kospi_list():
    kospi = pd.read_csv('data/KOSPI-20230319.csv', encoding = 'cp949',
                        dtype = {'종목코드':'str'})
    return kospi

def kosdaq_list():
    kosdaq = pd.read_csv('data/KOSDAQ-20230319.csv', encoding = 'cp949',
                         dtype = {'종목코드':'str'})
    return kosdaq

def finance(code):
    df = pd.read_html(f"https://finance.naver.com/item/main.naver?code={code}",
                      encoding = 'cp949')

    finance_df = df[3]

    finance_df = finance_df.droplevel([0,2],axis=1)
    finance_df.index = finance_df.iloc[:,0]
    # fiannce_df = finance_df.drop('주요재무정보',axis=1)
    yearly = finance_df.iloc[:,:5]
    quarterly = finance_df.iloc[:,5:]
    
    return yearly, quarterly

def peer(code):
    df = pd.read_html(f"https://finance.naver.com/item/main.naver?code={code}",
                      encoding = 'cp949')
    peer_df = df[4]
    peer_df = peer_df.set_index('종목명')
    
    return peer_df