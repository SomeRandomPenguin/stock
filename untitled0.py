import pandas as pd 
import pandas_datareader.data as web
from sqlalchemy import create_engine

con = create_engine('mysql+pymysql://root:django@34.210.26.166:58936/stock')


def download_price(code, start, end):
    df = web.DataReader(code, 'naver', start=start,end=end)
    df = df.astype('int')
    
    df = df.reset_index()
    df['code'] = code
    #print(df)
    df.to_sql('korea_prices',con,if_exists='append',index=False)
    return df
    



def get_codes(num_codes = 10):
    query = f'''
            SELECT 종목코드 FROM stock.info 
            order by 상장일
            Limit {num_codes}
            '''
    df = pd.read_sql(query,con)
    return df['종목코드'].values

def multi_download(codes, start, end):
    for code in codes:
        print(code)
        download_price(code, start, end)
        

codes = get_codes()
multi_download(codes, '20180101','20230707')



stock1 = download_price('06350','20230101','20230707')
rtn = stock1.loc[-1,'Close']/stock1.loc[0,'Close'][0] =1