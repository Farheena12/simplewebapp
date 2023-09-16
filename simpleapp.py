#import libraries streamlit yfinance pandas
import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
 #  Simple Stock Price App           

 Shown are the ***Closing price*** and ***Volume*** of Tesla!

""")

#define the ticker symbol
tickerSymbol = 'TSLA'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2022-1-1', end='2023-9-3')

col1, col2 = st.beta_columns([1,2])
with col1:
# Ticker image
        stock_logo = '<img src=%s>' % tickerData.info['logo_url']
        st.markdown(stock_logo, unsafe_allow_html=True )

        stock_name = tickerData.info['longName']
        st.header('**%s**' % stock_name)

with col2:
    st.write("""
    **Credits**

    ###App built by Farheena Khatib
    
    """)

st.subheader("Close chart")
st.line_chart(tickerDf.Close)

st.subheader("Volume chart")
st.line_chart(tickerDf.Volume)

