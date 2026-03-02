import numpy as np
from sklearn.metrics import mean_squared_error

def evaluate_model(actual, predicted):
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    return rmse

def trading_strategy(actual, forecast):
    signals = []

    for i in range(len(forecast)):
        if forecast[i] > actual[i]:
            signals.append(1)  # Buy
        else:
            signals.append(-1) # Sell

    return signals

