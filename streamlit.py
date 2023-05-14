# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import db
import numpy as np
import DataLoader as dl
import prophet_test as pt
import forecast 

st.title("Stocks Korea")
con = create_engine('mysql+pymysql://root:django@34.210.26.166:58936/stock') #data


name = db.name() #load code 


code2 = st.selectbox("Automatic input",(name))  #input


code1 = code2.split('-')[1].replace(' ','') #split data
df = db.info1(code1) #load code 

price_df = dl.korea_stock(code1, '2020-01-01','2023-04-16')


yearly,quarterly = db.finance(code1)
peer = db.peer(code1)

if(len(df)==1):     #empty check
    st.write("")
    st.subheader("회사명: "+df['회사명'][0])#print data
    st.write("업종: "+df['업종'][0])#print data
    st.write("주요제품: "+df['주요제품'][0])#print data
    st.write("대표자명: "+df['대표자명'][0])#print data
    try:
        st.write("홈페이지: "+df['홈페이지'][0])#print data
    except:
        st.write("홈페이지: X")#print data
else:
    st.write('ERROR: wrong code')#error


st.line_chart(price_df['Close'])#graph
fig = forecast.forecast(code1)
st.pyplot(fig)
st.write(yearly)
st.write(quarterly)
st.write(peer)













    
    # code1 = st.text_input("Manual input",placeholder="Enter name or code")

# if code2 != "":
#     df = db.info2(code2)
# else:
#     try:
#         int(code1)
#         try:
#             df = db.info1(code1)
#         except:
#             st.write('ERROR: wrong code')
#     except:
#         try:
#             df = db.info2(code1)
#         except:
#             if code1 == "":
#                 st.write("Input is Empty")
#             else:
#                 st.write("ERROR: wrong code")