import pandas as pd

def trip_distance(df: pd.DataFrame) -> pd.Series:
    """
    Cheap feature: raw trip distance
    """
    return df["trip_distance"]


def trip_duration_minutes(df: pd.DataFrame) -> pd.Series:
    """
    Cheap feature: trip duration in minutes
    """
    pickup = pd.to_datetime(df["tpep_pickup_datetime"])
    dropoff = pd.to_datetime(df["tpep_dropoff_datetime"])
    duration = (dropoff - pickup).dt.total_seconds() / 60.0
    return duration
