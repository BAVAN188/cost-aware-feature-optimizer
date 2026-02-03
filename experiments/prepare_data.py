import pandas as pd

# Load data
df = pd.read_csv("data/raw/taxi_sample.csv")

# Create trip duration in minutes
pickup = pd.to_datetime(df["tpep_pickup_datetime"])
dropoff = pd.to_datetime(df["tpep_dropoff_datetime"])
df["trip_duration_minutes"] = (dropoff - pickup).dt.total_seconds() / 60.0

# Create label: long trip or not
df["is_long_trip"] = (df["trip_duration_minutes"] >= 20).astype(int)

# Keep only useful columns
columns = [
    "trip_distance",
    "trip_duration_minutes",
    "is_long_trip"
]

df = df[columns]

# Save processed data
df.to_csv("data/processed_day2.csv", index=False)

print("Prepared data saved to data/processed_day2.csv")
