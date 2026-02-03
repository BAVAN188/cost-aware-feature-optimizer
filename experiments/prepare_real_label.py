import pandas as pd

df = pd.read_csv("data/raw/taxi_sample.csv")

# Parse times
df["pickup_dt"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["dropoff_dt"] = pd.to_datetime(df["tpep_dropoff_datetime"])

# Trip duration
df["trip_duration_min"] = (
    df["dropoff_dt"] - df["pickup_dt"]
).dt.total_seconds() / 60

# Zone-based SLA: 95th percentile duration per pickup zone
zone_p95 = (
    df.groupby("PULocationID")["trip_duration_min"]
      .quantile(0.95)
)

df["zone_p95"] = df["PULocationID"].map(zone_p95)

# SLA violation label (NO leakage)
df["sla_violation"] = (df["trip_duration_min"] > df["zone_p95"]).astype(int)

# Drop unsafe columns
df = df.drop(columns=[
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "zone_p95"
])


df.to_csv("data/processed_sla.csv", index=False)

print("Saved data/processed_sla.csv")
