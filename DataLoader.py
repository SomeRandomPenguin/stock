# -*- coding: utf-8 -*-

import pandas_datareader.data as web
import pandas as pd

# df = web.DataReader('065350','naver')

# df.dtypes

# df = df.astype('int')
# df.dtypes

# df['Close'].plot()

def korea_stock(code, start, end=None):
    df = pd.DataFrame()
    if end is None:
        df = web.DataReader(code, 'naver', start=start)
    else:
        df = web.DataReader(code, 'naver', start=start,end=end)
    df = df.astype('int')
    return df

# ss = korea_stock('065350','2020-01-01','2023-03-12')
# ss.Close.plot()


# df2 = web.DataReader('035420','naver')

# df2.dtypes

# df2 = df2.astype('int')
# df2.dtypes

# df2['Close'].plot()
# def korea_stock2(code, start, end):
#     df = web.DataReader(code, 'naver', start=start,end=end)
#     df = df.astype('int')
#     return df

# ss2 = korea_stock('035420','2018-01-01','2023-03-18')
# ss2.Close.plot()


def kospi_list():
    kospi = pd.read_csv('data/KOSPI-20230319.csv', encoding = 'cp949',
                        dtype = {'종목코드':'str'})
    return kospi

def kosdaq_list():
    kosdaq = pd.read_csv('data/KOSDAQ-20230319.csv', encoding = 'cp949',
                         dtype = {'종목코드':'str'})
    return kosdaq