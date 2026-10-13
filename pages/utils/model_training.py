from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller, kpss
import pandas as pd
from sklearn.preprocessing import StandardScaler
from datetime import timedelta


def get_data(ticker, start_date, end_date):
    import yfinance as yf
    data = yf.download(ticker, start=start_date, end=end_date)
    data.columns = data.columns.droplevel(level=1)
    return data['Close']


def stationary_check(close_prices):
    adf_results = adfuller(close_prices)
    kpss_results = kpss(close_prices, regression='c', nlags='auto')
    if adf_results[1] < 0.05 and kpss_results[1] > 0.05:
        return True
    else:
        return False


def smoothen_data(close_prices, window=7):
    roll_price = close_prices.rolling(window=window).mean().dropna()
    return roll_price


def train_arima_model(model, smooth_data, steps=7):
    model = ARIMA(smooth_data, order=model.order, seasonal_order=model.seasonal_order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    return forecast


def evaluate_model(model, org_prices):
    train, test = org_prices[:-30], org_prices[-30:]
    predictions = train_arima_model(model, train, steps=30)
    predictions.index = test.index
    rmse = ((predictions - test) ** 2).mean() ** 0.5
    return rmse


def scaling(close_prices):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(close_prices.values.reshape(-1, 1))
    return scaled_data, scaler


def get_forecast(model, scaled_prices, steps=7):
    predictions = train_arima_model(model, scaled_prices, steps=steps)
    start_date = scaled_prices.index[-1] + timedelta(days=1)
    end_data = scaled_prices.index[-1] + timedelta(days=steps)
    date_range = pd.date_range(start=start_date, end=end_data)
    forecast_df = pd.DataFrame(predictions.values, index=date_range, columns=['Close'])
    return forecast_df


def inverse_scaling(scaled_data, scaler):
    org_data = scaler.inverse_transform(scaled_data)
    return org_data


def bst_params(close_prices):
    from pmdarima import auto_arima
    model = auto_arima(
        close_prices,
        start_p=1,
        start_q=1,
        max_p=5,
        max_q=5,
        m=12,
        seasonal=True,
        d=None,
        trace=True,
        error_action='ignore',
        suppress_warnings=True,
        stepwise=True,
    )
    return model
