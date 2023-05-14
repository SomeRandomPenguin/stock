# -*- coding: utf-8 -*-
import DataLoader as dl
from sqlalchemy import create_engine
import pandas as pd



kospi = dl.kospi_list()
kospi['거래소']='kospi'


kosdaq = dl.kosdaq_list()
kosdaq['거래소']='kosdaq'



result = pd.concat([kospi,kosdaq])

con = create_engine('mysql+pymysql://root:django@34.210.26.166:58936/stock')

result.to_sql('info', con, if_exists = 'replace', index = False)