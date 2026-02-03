import pandas as pd

def pickup_hour(df):
    return pd.to_datetime(df["pickup_dt"]).dt.hour

def trip_distance(df):
    return df["trip_distance"]
