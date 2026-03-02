import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from timegpt_model import run_timegpt
from lstm_model import run_lstm
from backtest import evaluate_model
from portfolio import optimize_portfolio

st.title("AI Stock Forecasting & Quant System")

api_key = st.text_input("Enter Nixtla API Key")

stock = st.selectbox("Select Stock", ["AAPL", "TSLA", "MSFT"])
model_choice = st.selectbox("Select Model", ["TimeGPT", "LSTM"])

df = yf.download(stock, start="2020-01-01")
df = df.reset_index()[['Date','Close']]
df.columns = ['ds','y']

st.line_chart(df.set_index("ds")['y'])

if st.button("Run Forecast"):

    horizon = 30

    if model_choice == "TimeGPT":
        forecast = run_timegpt(df, api_key, horizon)
        forecast_values = forecast['TimeGPT']
        future_dates = forecast['ds']

    else:
        forecast_values = run_lstm(df, horizon)
        future_dates = pd.date_range(df['ds'].iloc[-1], periods=horizon+1)[1:]

    st.subheader("Forecast Result")

    fig, ax = plt.subplots()
    ax.plot(df['ds'], df['y'], label="Actual")
    ax.plot(future_dates, forecast_values, label="Forecast")
    ax.legend()
    st.pyplot(fig)

    rmse = evaluate_model(df['y'][-horizon:], forecast_values[:horizon])
    st.write("RMSE:", rmse)

# Portfolio Section
st.subheader("Portfolio Optimization")

stocks = ["AAPL","TSLA","MSFT"]
returns_data = pd.DataFrame()

for s in stocks:
    data = yf.download(s, start="2022-01-01")['Close']
    returns_data[s] = data.pct_change()

returns_data.dropna(inplace=True)

weights = optimize_portfolio(returns_data)

st.write("Optimal Portfolio Weights:")
for i, s in enumerate(stocks):
    st.write(s, ":", round(weights[i],2))