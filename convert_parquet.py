import pandas as pd
import os

# Read parquet from project root
df = pd.read_parquet("yellow_tripdata_2024-12.parquet")

# Take a small sample
df_sample = df.sample(n=20000, random_state=42)

# Make sure folders exist
os.makedirs("data/raw", exist_ok=True)

# Write CSV with real data
df_sample.to_csv("data/raw/taxi_sample.csv", index=False)

print("CSV created at data/raw/taxi_sample.csv")
