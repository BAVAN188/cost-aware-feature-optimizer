import time
import pandas as pd
from features.window_features import rolling_trip_count

df = pd.read_csv("data/processed_sla.csv")

# Ensure datetime
df["pickup_dt"] = pd.to_datetime(df["pickup_dt"])

start = time.perf_counter()
_ = rolling_trip_count(df)
end = time.perf_counter()

print(f"Rolling window feature latency: {(end-start)*1000:.2f} ms")
