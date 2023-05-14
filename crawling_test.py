# -*- coding: utf-8 -*-
import pandas as pd 


df = pd.read_html('https://finance.naver.com/item/main.naver?code=065350',
                  encoding = 'cp949')

finance_df = df[3]

finance_df = finance_df.droplevel([0,2],axis=1)
finance_df.index = finance_df.iloc[:,0]
fiannce_df = finance_df.drop('주요재무정보',axis=1)
yearly = finance_df.iloc[:,:5]
quarterly = finance_df.iloc[:,5:]


print(yearly.loc['매출액','2020.12'])


compare_df = df[4]
compare_df.index = compare_df.iloc[:,0]
compare_df = compare_df.drop('종목명',axis=1)