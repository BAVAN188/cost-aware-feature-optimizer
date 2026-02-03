import time
import pandas as pd
from features.window_features import (
    rolling_trip_count,
    rolling_avg_duration,
    rolling_trip_fare_sum,
)

df = pd.read_csv("data/processed_sla.csv")
df["pickup_dt"] = pd.to_datetime(df["pickup_dt"])

features = {
    "rolling_trip_count": rolling_trip_count,
    "rolling_avg_duration": rolling_avg_duration,
    "rolling_trip_fare_sum": rolling_trip_fare_sum,
}

for name, fn in features.items():
    start = time.perf_counter()
    _ = fn(df)
    end = time.perf_counter()
    print(f"{name}: {(end-start)*1000:.2f} ms")
