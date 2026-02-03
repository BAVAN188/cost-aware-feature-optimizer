FEATURES = {
    "trip_distance": {
        "cost_ms": 0.2,
        "accuracy": 0.825
    },
    "trip_duration_minutes": {
        "cost_ms": 20.0,
        "accuracy": 0.999
    }
}

LATENCY_BUDGET_MS = 20.0
MIN_ACCURACY = 0.99

selected = []

for name, info in FEATURES.items():
    if info["cost_ms"] <= LATENCY_BUDGET_MS and info["accuracy"] >= MIN_ACCURACY:
        selected.append(name)

print("Recommended features:", selected)
