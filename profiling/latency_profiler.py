import time
import pandas as pd
from features.base_features import trip_distance, trip_duration_minutes

# Load data
df = pd.read_csv("data/raw/taxi_sample.csv")

def profile_feature(fn, name, runs=10):
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        _ = fn(df)
        end = time.perf_counter()
        times.append((end - start) * 1000)  # ms

    times.sort()
    mean_ms = sum(times) / len(times)
    p95_ms = times[int(0.95 * len(times))]

    print(f"{name}: mean={mean_ms:.2f} ms, p95={p95_ms:.2f} ms")


if __name__ == "__main__":
    profile_feature(trip_distance, "trip_distance")
    profile_feature(trip_duration_minutes, "trip_duration_minutes")
