from nixtla import NixtlaClient
import pandas as pd

def run_timegpt(df, api_key, horizon=30):

    df['ds'] = pd.to_datetime(df['ds'])

    df = df.drop_duplicates(subset=['ds'])

    df = df.sort_values('ds').reset_index(drop=True)

    df = df.set_index('ds')

    df = df.asfreq('B')

    df['y'] = df['y'].fillna(method='ffill')

    df = df.reset_index()

    client = NixtlaClient(api_key=api_key)

    forecast = client.forecast(
        df=df,
        h=horizon,
        freq='B'
    )

    return forecast

