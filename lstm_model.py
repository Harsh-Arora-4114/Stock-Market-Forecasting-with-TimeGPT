import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def run_lstm(df, horizon=30):

    data = df['y'].values.reshape(-1,1)

    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    X, y = [], []
    window = 60

    for i in range(window, len(data_scaled)):
        X.append(data_scaled[i-window:i])
        y.append(data_scaled[i])

    X, y = np.array(X), np.array(y)

    model = Sequential()
    model.add(LSTM(50, return_sequences=False, input_shape=(window,1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    model.fit(X, y, epochs=5, batch_size=32, verbose=0)

    last_window = data_scaled[-window:]
    current_batch = last_window.reshape(1, window, 1)

    preds = []

    for _ in range(horizon):

        pred = model.predict(current_batch, verbose=0)
        preds.append(pred[0][0])

        pred_reshaped = pred.reshape(1, 1, 1)

        current_batch = np.concatenate(
            (current_batch[:, 1:, :], pred_reshaped),
            axis=1
        )

    preds = scaler.inverse_transform(
        np.array(preds).reshape(-1,1)
    )

    return preds.flatten()

