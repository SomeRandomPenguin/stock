# -*- coding: utf-8 -*-

import DataLoader as dl


shinsung_df = dl.korea_stock('065350', '2020-01-01', '2023-03-12')
shinsung_df.Close.plot()


kospi = dl.kospi_list()
kosdaq = dl.kosdaq_list()


code = kospi['종목코드'][0]
dl.korea_stock(code,'2020-01-01', '2023-03-18')




kospi_list = []
kosdaq_list = []

for i in range (0,10):
    code = kospi['종목코드'][i]
    r = dl.korea_stock(code,'2020-01-01', '2023-03-18')
    kospi_list.append(r)
    
for t in range (0,10):
    code = kospi['종목코드'][t]
    r = dl.korea_stock(code,'2020-01-01', '2023-03-18')
    kosdaq_list.append(r)
    
from sqlalchemy import create_engine
con = create_engine('mysql+pymysql://root:django@34.210.26.166:58936/stock')
kospi.to_sql('kospi', con, if_exists='replace')
kosdaq.to_sql('kosdaq', con, if_exists='replace')



s = dl.korea_stock('035420','2018-01-01','2023-03-18')
s.to_sql('ssdt', con, if_exists='replace')

import pandas as pd 
query  = 'SELECT 회사명, 종목코드 FROM stock.kospi;'
df = pd.read_sql(query, con)