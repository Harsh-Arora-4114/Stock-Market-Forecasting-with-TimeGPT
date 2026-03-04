# Stock Market Forecasting


## Overview

This project focuses on forecasting stock prices and optimizing investment portfolios using Artificial Intelligence and Quantitative Finance techniques. The system integrates:

* **TimeGPT (Nixtla API)** – Foundation model for time-series forecasting
* **LSTM (Deep Learning Model)** – Custom neural network forecasting
* **Backtesting with RMSE evaluation**
* **Modern Portfolio Theory (MPT) Optimization**
* **Streamlit Interactive Dashboard**

The application allows users to:
* Forecast future stock prices
* Compare AI models (TimeGPT vs LSTM)
* Evaluate prediction accuracy
* Generate simple trading signals
* Optimize portfolio allocation

This is a complete AI + Quant Finance project suitable for research, academic work, and resume portfolios.

---

## Objectives

* Develop an AI-powered stock forecasting system
* Implement LSTM-based time-series prediction
* Integrate Nixtla’s TimeGPT API
* Evaluate models using RMSE
* Perform portfolio optimization using volatility minimization
* Build an interactive financial analytics dashboard

---

## Key Features

### Stock Forecasting

* Historical data download using Yahoo Finance
* 30-day future price prediction
* Model comparison: TimeGPT vs LSTM
* Actual vs forecast visualization

### TimeGPT API Integration

* Uses Nixtla’s foundation time-series model
* No training required
* Requires API key
* Fast and production-ready forecasting

### LSTM Deep Learning Model

* 60-day rolling window
* MinMax scaling
* 50 LSTM units
* Recursive multi-step forecasting

### Model Evaluation

* Root Mean Squared Error (RMSE)
* Forecast comparison with actual prices
* Basic trading signal logic (Buy/Sell)

### Portfolio Optimization

* Uses daily returns
* Computes covariance matrix
* Minimizes portfolio volatility
* Constraints:

  * Weights sum to 1
  * No short selling (0 ≤ weight ≤ 1)

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
| Forecasting API      | Nixtla TimeGPT     |

---

### Why TimeGPT?

* Pretrained foundation model
* No manual deep learning training required
* Automatically captures trend & seasonality
* Works well for financial time series

---

## Project Workflow

### 1. Data Collection & Preprocessing

* Download stock prices (from 2020)
* Select closing prices
* Format for time-series models
* Scale data for LSTM

### 2. Data Visualization

* Plot historical stock trends
* Understand price movement

### 3. Model Development

#### LSTM Model

* Convolution-free sequential model
* 60-day input window
* Dense output layer

#### TimeGPT Model

* API-based forecasting
* External foundation model

### 4. Model Evaluation

* Calculate RMSE
* Compare actual vs predicted values
* Generate trading signals

### 5. Portfolio Optimization

* Compute daily returns
* Calculate covariance matrix
* Minimize portfolio volatility
* Generate optimal asset weights

---

## Sample Results

Forecast Horizon: 30 Days

Outputs:

* Predicted future stock prices
* RMSE score
* Optimal portfolio allocation

Key Insights:

* LSTM captures short-term patterns effectively
* TimeGPT performs strongly without custom training
* Diversification reduces portfolio volatility

---

## How to Run

### 1.  Clone Repository

```bash
git clone https://github.com/yourusername/AI-Stock-Forecasting-System.git
cd AI-Stock-Forecasting-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt not available:

```bash
pip install streamlit yfinance pandas numpy matplotlib tensorflow scikit-learn scipy
```

### 3. Run Application

```bash
python -m streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

### 4. Using TimeGPT

* Enter Nixtla API key
* Select TimeGPT
* Click "Run Forecast"

---

## Future Scope

* Add Sharpe Ratio maximization
* Add Monte Carlo simulation
* Add multi-asset dynamic selection
* Add risk-adjusted performance metrics
* Deploy on Streamlit Cloud / AWS
* Add advanced backtesting (strategy returns, CAGR, drawdown)

---

## Applications

* Quantitative Finance Research
* AI in Financial Markets
* Resume Project (ML Engineer / Data Scientist / Quant Developer)
* Academic AI + Finance Integration

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by **Harsh Arora**
