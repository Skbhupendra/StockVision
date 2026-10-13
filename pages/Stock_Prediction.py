import datetime
import streamlit as st
import pandas as pd
from pages.utils.plotly_fig import forecast_moving_average
from pages.utils.model_training import get_data, get_forecast, evaluate_model, scaling, inverse_scaling, smoothen_data, bst_params

# page configuration, visible in the browser tab
st.set_page_config(
    page_title='Stock Prediction Page',
    page_icon='🤖',
    layout='wide'
)

st.title("🤖 Stock Prediction")
c1, c2 = st.columns(2)
with c1:
    ticker = st.selectbox("Select Ticker", options=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'JPM', 'V', 'UNH'])
with c2:
    steps = st.number_input('Enter the number of days to forecast in Future', min_value=1, max_value=30, value=7, step=1)

today_date = datetime.date.today()
close_prices = get_data(ticker, today_date - datetime.timedelta(days=365), today_date)

rolling_price = smoothen_data(close_prices, steps)
model = bst_params(close_prices)
scaled_data, scaler = scaling(rolling_price)
scaled_data_df = pd.DataFrame(scaled_data, index=rolling_price.index, columns=['Close'])
rmse = evaluate_model(model, close_prices)
forecast_df = get_forecast(model, scaled_data_df, steps=steps)
forecast_inv = inverse_scaling(forecast_df.values, scaler)
forecast_inv_df = pd.DataFrame(forecast_inv, index=forecast_df.index, columns=['Close'])

st.markdown(f"### Predicted Stock Prices for next {steps} days for {ticker}")

forecast = pd.concat([close_prices, forecast_inv_df], axis=0)
fig = forecast_moving_average(forecast, window=steps)
st.plotly_chart(fig, width='stretch')

forecast.index.name = 'Date'
forecast = forecast.reset_index()

st.subheader('Forecast Preview')
st.dataframe(forecast.tail(50), use_container_width=True)
