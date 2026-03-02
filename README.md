# Stock-Market-Forecasting-with-TimeGPT

---

## Overview

This project focuses on forecasting stock prices and optimizing portfolios using Artificial Intelligence and Quantitative Finance techniques. The system integrates Deep Learning (LSTM), AI-based Time Series Forecasting (TimeGPT), Backtesting, and Modern Portfolio Theory to create an end-to-end financial analytics platform.

The application is built using **Streamlit** for an interactive user interface and allows users to:

* Forecast stock prices (AAPL, TSLA, MSFT)
* Compare AI models (TimeGPT vs LSTM)
* Evaluate prediction accuracy using RMSE
* Optimize portfolio weights using volatility minimization

This project combines Machine Learning, Financial Engineering, and Data Science into one scalable system.

---

## Objectives

* Build an AI-powered stock forecasting system.
* Implement LSTM-based deep learning for time series prediction.
* Integrate TimeGPT API for advanced forecasting.
* Evaluate model performance using RMSE.
* Implement portfolio optimization using Modern Portfolio Theory.
* Create an interactive web dashboard using Streamlit.

---

## Key Features

### Stock Forecasting

* Historical data download using Yahoo Finance API
* 30-day future price prediction
* Model comparison: TimeGPT vs LSTM
* Visual forecast vs actual comparison

### Model Evaluation

* RMSE (Root Mean Squared Error) calculation
* Basic trading signal logic (Buy/Sell indicator)

### Portfolio Optimization

* Uses covariance matrix & mean returns
* Minimizes portfolio volatility
* Weight constraints: No short selling (0–1 range)
* Fully invested portfolio (weights sum to 1)

### Expandability

* Add more stocks dynamically
* Add Sharpe Ratio optimization
* Add Monte Carlo simulation
* Deploy to cloud

---

## Technologies Used

| Category             | Tools / Libraries  |
| -------------------- | ------------------ |
| Programming Language | Python             |
| Web Framework        | Streamlit          |
| Data Source          | yFinance           |
| Deep Learning        | TensorFlow / Keras |
| Data Processing      | NumPy, Pandas      |
| Optimization         | SciPy              |
| Evaluation           | Scikit-learn       |
| Visualization        | Matplotlib         |

---

## Dataset

Stock price data is fetched dynamically using Yahoo Finance API.

Example stocks used:

* Apple (AAPL)
* Tesla (TSLA)
* Microsoft (MSFT)

Data preprocessing:

* Reset index
* Rename columns to time-series format (`ds`, `y`)
* Percentage return calculation for portfolio optimization
* Train horizon: 30 days

---

## Project Workflow

### 1. Data Collection & Preprocessing

* Download stock data from 2020 onward
* Select closing prices
* Convert into time series format
* Normalize data for LSTM

### 2. Exploratory Data Visualization

* Line chart of historical stock prices
* Trend visualization before forecasting

### 3. Model Development

#### LSTM Model

* 60-day rolling window
* MinMax Scaling
* 50 LSTM units
* Dense output layer
* Recursive forecasting

#### TimeGPT Model

* API-based forecasting
* Advanced time-series AI model

### 4. Model Training & Evaluation

* Loss: Mean Squared Error
* Optimizer: Adam
* RMSE calculation
* Forecast vs actual comparison

### 5. Portfolio Optimization

* Calculate daily returns
* Compute covariance matrix
* Minimize portfolio volatility
* Generate optimal weight allocation

---

## Sample Results

Forecast Horizon: 30 Days

Evaluation Metric: RMSE

Outputs:

* Predicted future stock prices
* RMSE score
* Optimal portfolio weights for AAPL, TSLA, MSFT

Key Insights:

* LSTM captures short-term trends effectively
* TimeGPT performs well for structured time series
* Diversified portfolios reduce volatility

---

## Applications

* Quantitative Research Projects
* Financial Data Science Portfolio
* AI-based Trading Research
* Academic ML + Finance Integration
* Resume Project for Data Analyst / ML Engineer / Quant Developer

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Stock-Forecasting-System.git
cd AI-Stock-Forecasting-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit yfinance pandas numpy matplotlib tensorflow scikit-learn scipy
```

### 3. Run the application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

### 4. Using TimeGPT (Optional)

* Enter Nixtla API key
* Select TimeGPT model
* Click "Run Forecast"

---

## Future Scope

* Add Sharpe Ratio maximization
* Add Monte Carlo simulation
* Add live market streaming
* Implement risk-adjusted metrics
* Deploy on Streamlit Cloud / AWS
* Add automated backtesting with strategy returns

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by **Harsh Arora**
