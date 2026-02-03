import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load processed data
df = pd.read_csv("data/processed_day2.csv")

X = df[["trip_distance", "trip_duration_minutes"]]
y = df["is_long_trip"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print(f"Accuracy with BOTH features: {acc:.3f}")
