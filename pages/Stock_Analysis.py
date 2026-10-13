import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
from pages.utils.plotly_fig import plotly_table, line_chart, candlestick, RSI, SMA, EMA, MACD

# page configuration, visible in the browser tab
st.set_page_config(
    page_title='Stock Analysis Page',
    page_icon='📊',
    layout='wide'
)

st.title("📊 Stock Analysis")
# input part
today = datetime.date.today()
c1, c2, c3 = st.columns([3, 3, 3])
with c1:
    ticker = st.selectbox("Enter Stock Ticker", placeholder='Select ticker', options=["AAPL", 'TSLA', 'MSFT', 'AMZN', 'GOOGL', 'META', 'NVDA', 'JPM', 'V', 'UNH'])
with c2:
    start_data = st.date_input('Start Date', today - datetime.timedelta(days=365))
with c3:
    end_date = st.date_input('End Date', today)

# information section
if ticker:
    tkr_name = ticker
    st.subheader(f"{tkr_name} ")
    stock_info = yf.Ticker(ticker)
    st.write(stock_info.info['longBusinessSummary'])
    st.write("**Sector:**", stock_info.info['sector'])
    st.write("**Industry:**", stock_info.info['industry'])
    st.write("**Full-time Employees:**", stock_info.info['fullTimeEmployees'])
    st.write("**Website:**", stock_info.info['website'])

# creating tables and plots
col1, col2 = st.columns([1, 1])
with col1:
    df = pd.DataFrame(index=['Market Cap', 'Beta', 'EPS', 'PE Ratio'])
    df[''] = [stock_info.info['marketCap'], stock_info.info['beta'], stock_info.info['trailingEps'], stock_info.info['trailingPE']]
    st.table(df)
with col2:
    df = pd.DataFrame(index=['Quick Ratio', 'Revenue Per Share', 'Profit Margin', 'Debt to Equity', 'Return on Equity'])
    df[''] = [stock_info.info['quickRatio'], stock_info.info['revenuePerShare'], stock_info.info['profitMargins'], stock_info.info['debtToEquity'], stock_info.info['returnOnEquity']]
    st.table(df)

# data fetching part
data = yf.download(ticker, start=start_data, end=end_date)
data.columns = data.columns.droplevel(level=1)
c1, c2, c3 = st.columns([1, 1, 1])
c1.metric("Opening Price", f"${data['Open'][-1]:.2f}", f"{data['Open'][-1]-data['Open'][-2]:.2f}")
c2.metric("Closing Price", f"${data['Close'][-1]:.2f}", f"{data['Close'][-1]-data['Close'][-2]:.2f}")
c3.metric("Daily Change", f"{((data['Close'][-1]-data['Close'][-2])/data['Close'][-2])*100:.2f}%", f"{data['Close'][-1]-data['Close'][-2]:.2f}")

# historical data
st.subheader(f"Historical Data For {tkr_name}")
st.write("Last 10 Days Data")
st.table(data.iloc[:, 1:].tail(10))

# adding multiple buttons for interactive data view
c1, c2, c3, c4, c5, c6 = st.columns([1, 1, 1, 1, 1, 1])
periods = ''
with c1:
    if st.button('7D'):
        periods = '7d'
with c2:
    if st.button('1M'):
        periods = '1mo'
with c3:
    if st.button('3M'):
        periods = '3mo'
with c4:
    if st.button('6M'):
        periods = '6mo'
with c5:
    if st.button('1Y'):
        periods = '1y'
with c6:
    if st.button('Max'):
        periods = 'max'

c1, c2, c3 = st.columns([1, 1, 4])
with c1:
    chart_type = st.selectbox('Select Chart Type', ['Line', 'Candlestick'])
with c2:
    if chart_type == 'Line':
        indicators = st.selectbox('Select Indicator', ['SMA', 'EMA', 'RSI', 'MACD'])
    else:
        indicators = st.selectbox('Select Indicator', ['SMA', 'EMA'])

if periods == '':
    periods = '1y'

if chart_type == 'Line' and indicators == 'RSI':
    fig = line_chart(data, periods)
    st.plotly_chart(fig, width='stretch')
    st.write(f"**{indicators} for {tkr_name}**")
    fig = RSI(data, periods=periods)
    st.plotly_chart(fig, width='stretch')
elif chart_type == 'Line' and indicators == 'SMA':
    fig = line_chart(data, periods)
    st.plotly_chart(fig, width='stretch')
    st.write(f"**{indicators} for {tkr_name}**")
    fig = SMA(data, periods=periods)
    st.plotly_chart(fig, width='stretch')
elif chart_type == 'Line' and indicators == 'EMA':
    fig = line_chart(data, periods)
    st.plotly_chart(fig, width='stretch')
    st.write(f"**{indicators} for {tkr_name}**")
    fig = EMA(data, periods=periods)
    st.plotly_chart(fig, width='stretch')
elif chart_type == 'Line' and indicators == 'MACD':
    fig = line_chart(data, periods)
    st.plotly_chart(fig, width='stretch')
    st.write(f"**{indicators} for {tkr_name}**")
    fig = MACD(data, periods=periods)
    st.plotly_chart(fig, width='stretch')
elif chart_type == 'Candlestick' and indicators == 'SMA':
    fig = candlestick(data, periods)
    st.plotly_chart(fig, width='stretch')
    st.write(f'**{indicators} for {tkr_name}**')
    fig = SMA(data, periods=periods)
    st.plotly_chart(fig, width='stretch')
elif chart_type == 'Candlestick' and indicators == 'EMA':
    fig = candlestick(data, periods)
    st.plotly_chart(fig, width='stretch')
    st.write(f'**{indicators} for {tkr_name}**')
    fig = EMA(data, periods=periods)
    st.plotly_chart(fig, width='stretch')
