import streamlit as st
import yfinance as yf
import plotly.express as px


# Function to fetch stock data from Yahoo Finance API
def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d", interval="5m")
    return data[['Close']].reset_index()

# App Layout
st.title("Real-Time Stock Price Dashboard")


symbol = st.text_input('Enter Stock Symbol (e.g. AAPL, TSLA)', 'AAPL')

# Button to fetch stock data
if st.button('Get Stock Data'):
    if symbol:
        stock_data = fetch_stock_data(symbol)
        st.subheader(f"Real-Time Data for {symbol}")
        st.write(stock_data)

# Plotting stock data
        fig = px.line(stock_data, x='Datetime', y='Close', title=f'{symbol} Stock Price')
        st.plotly_chart(fig)
    else:
        st.error("Please provide a valid stock symbol.")
