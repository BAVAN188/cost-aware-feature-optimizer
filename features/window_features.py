import pandas as pd

def rolling_trip_count(df, window="30min"):
    df = df.sort_values("pickup_dt")

    return (
        df
        .set_index("pickup_dt")
        .groupby("PULocationID")["trip_distance"]
        .rolling(window)
        .count()
        .reset_index(level=0, drop=True)
    )
def rolling_avg_duration(df, window="30min"):
    df = df.sort_values("pickup_dt")
    return (
        df
        .set_index("pickup_dt")
        .groupby("PULocationID")["trip_duration_min"]
        .rolling(window)
        .mean()
        .reset_index(level=0, drop=True)
    )


def rolling_trip_fare_sum(df, window="30min"):
    df = df.sort_values("pickup_dt")
    return (
        df
        .set_index("pickup_dt")
        .groupby("PULocationID")["total_amount"]
        .rolling(window)
        .sum()
        .reset_index(level=0, drop=True)
    )
