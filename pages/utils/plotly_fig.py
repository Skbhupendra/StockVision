import plotly.graph_objects as go
import dateutil
import pandas_ta as pta


def plotly_table(dataframe):
    headerColor = 'grey'
    rowEvenColor = "#0f66e9"
    rowOddColor = "#ef9c1e"
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=["<b><b>" + "<b>" + str(i)[:10] + "<b>" for i in dataframe.columns],
            line_color='#0078ff', fill_color='#0078ff',
            align='center', font=dict(color='white', size=15), height=35,
        ),
        cells=dict(
            values=[["<b>" + str(i) + "<b>" for i in dataframe.index]] + [dataframe[i] for i in dataframe.columns],
            fill_color=[[rowOddColor, rowEvenColor] * len(dataframe.index)],
            align='left', line_color=['white'], font=dict(color=["black"], size=15)
        )
    )])
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=0, b=0))
    return fig


def filter_data(df, n_periods):
    if n_periods == '7d':
        date = df.index[-1] - dateutil.relativedelta.relativedelta(days=7)
    elif n_periods == '1mo':
        date = df.index[-1] - dateutil.relativedelta.relativedelta(months=1)
    elif n_periods == '3mo':
        date = df.index[-1] - dateutil.relativedelta.relativedelta(months=3)
    elif n_periods == '6mo':
        date = df.index[-1] - dateutil.relativedelta.relativedelta(months=6)
    elif n_periods == '1y':
        date = df.index[-1] - dateutil.relativedelta.relativedelta(years=1)
    else:
        date = df.index[0]
    mask = (df.index >= date) & (df.index <= df.index[-1])
    filtered_df = df.loc[mask]
    return filtered_df


def line_chart(df, n_periods=False):
    if n_periods:
        df = filter_data(df, n_periods)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Open'], mode='lines', name='Opening Price', line=dict(width=2, color='blue')))
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Closing Price', line=dict(width=2, color='orange')))
    fig.add_trace(go.Scatter(x=df.index, y=df['High'], mode='lines', name='High Price', line=dict(width=2, color='green')))
    fig.add_trace(go.Scatter(x=df.index, y=df['Low'], mode='lines', name='Low Price', line=dict(width=2, color='red')))
    fig.update_layout(title='Stock Prices Over Time', xaxis_title='Date', yaxis_title='Price', legend_title='Price Type', height=500, margin=dict(l=0, r=0, t=30, b=0))
    return fig


def candlestick(df, n_periods=False):
    if n_periods:
        df = filter_data(df, n_periods)
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                increasing_line_color='green',
                decreasing_line_color='red')])
    fig.update_layout(title='Candlestick Chart', xaxis_title='Date', yaxis_title='Price', height=500, margin=dict(l=0, r=0, t=30, b=0))
    return fig


def RSI(df, periods='7d'):
    df['rsi'] = pta.rsi(df['Close'], length=periods)
    df = filter_data(df, periods)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['rsi'], mode='lines', name='RSI', line=dict(width=2, color='purple')))
    fig.add_trace(go.Scatter(x=df.index, y=[70] * len(df), mode='lines', name='Overbought level(70)', line=dict(width=2, color='red', dash='dash')))
    fig.add_trace(go.Scatter(x=df.index, y=[30] * len(df), mode='lines', name='Oversold level(30)', line=dict(width=2, color='green', dash='dot')))
    fig.update_layout(title='Relative Strength Index (RSI)', xaxis_title='Date', yaxis_title='RSI', height=400, margin=dict(l=0, r=0, t=30, b=0))
    return fig


def SMA(df, periods='7d'):
    df['SMA'] = pta.sma(df['Close'], length=periods)
    df = filter_data(df, periods)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA'], mode='lines', name='SMA', line=dict(width=2, color='blue')))
    fig.add_trace(go.Scatter(x=df.index, y=df.Close, mode='lines', name='Closing Price', line=dict(width=1, color='orange', dash='dot')))
    fig.add_trace(go.Scatter(x=df.index, y=df.Open, mode='lines', name='Opening Price', line=dict(width=1)))
    fig.add_trace(go.Scatter(x=df.index, y=df.High, mode='lines', name='High Price', line=dict(width=1, color='green', dash='dot')))
    fig.add_trace(go.Scatter(x=df.index, y=df.Low, mode='lines', name='Low Price', line=dict(width=1, color='red', dash='dot')))
    fig.update_layout(title='Simple Moving Average (SMA)', xaxis_title='Date', yaxis_title='SMA', height=400, margin=dict(l=0, r=0, t=30, b=0))
    return fig


def MACD(df, periods='7d'):
    macd = pta.macd(df['Close']).iloc[:, 0]
    macd_signal = pta.macd(df['Close']).iloc[:, 1]
    macd_hist = pta.macd(df['Close']).iloc[:, 2]
    df['MACD'] = macd
    df['MACD_Signal'] = macd_signal
    df['MACD_Hist'] = macd_hist
    df = filter_data(df, periods)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], mode='lines', name='Macd', line=dict(width=2, color='blue')))
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD_Signal'], mode='lines', name='macd Signal', line=dict(width=2, color='orange')))
    fig.update_layout(title='Moving Average Convergence Divergence (MACD)', xaxis_title='Date', yaxis_title='MACD', height=400, margin=dict(l=0, r=0, t=30, b=0))
    return fig


def EMA(df, period='7d'):
    df['EMA'] = pta.ema(df['Close'], length=period)
    df = filter_data(df, period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['EMA'], mode='lines', name='EMA', line=dict(width=2, color='blue')))
    fig.add_trace(go.Scatter(x=df.index, y=df.Open, mode='lines', name='Opening Price', line=dict(width=1, color='orange', dash='dot')))
    fig.add_trace(go.Scatter(x=df.index, y=df.High, mode='lines', name='High Price', line=dict(width=1, color='green', dash='dot')))
    fig.add_trace(go.Scatter(x=df.index, y=df.Low, mode='lines', name='Low Price', line=dict(width=1, color='red', dash='dot')))
    fig.add_trace(go.Scatter(x=df.index, y=df.Close, mode='lines', name='Closing Price', line=dict(width=1, color='black', dash='dot')))
    fig.update_layout(title='Exponential Moving Average (EMA)', xaxis_title='Date', yaxis_title='EMA', height=400, margin=dict(l=0, r=0, t=30, b=0))
    return fig


def forecast_moving_average(forecast_df, window=7):
    forecast_df['Forecast_MA'] = pta.sma(forecast_df['Close'], length=window)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast_df.index[:-window + 1], y=forecast_df['Forecast_MA'], mode='lines', name='Previous Price', line=dict(width=2, color='yellow')))
    fig.add_trace(go.Scatter(x=forecast_df.index[-window:], y=forecast_df['Forecast_MA'][-window:], mode='lines', name='Forecasted Price', line=dict(width=2, color='red', dash='solid')))
    fig.update_layout(title='Forecasted Stock Prices using Moving Average', xaxis_title='Date', yaxis_title='Forecasted Price', height=400, margin=dict(l=0, r=0, t=30, b=0))
    return fig
