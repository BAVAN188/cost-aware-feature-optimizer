from optimizer.config import LATENCY_BUDGET_MS
from optimizer.feature_registry import FEATURES

selected = []
dropped = []
total_latency = 0.0
total_accuracy = 0.0

def score(item):
    name, meta = item
    return meta["accuracy_gain"] / meta["latency_ms"]

for name, meta in sorted(FEATURES.items(), key=score, reverse=True):
    if total_latency + meta["latency_ms"] <= LATENCY_BUDGET_MS:
        selected.append(name)
        total_latency += meta["latency_ms"]
        total_accuracy += meta["accuracy_gain"]
    else:
        dropped.append(name)

print("Latency budget:", LATENCY_BUDGET_MS, "ms")
print("Selected features:", selected)
print("Dropped features:", dropped)
print("Total latency:", round(total_latency, 2), "ms")
print("Expected accuracy gain:", round(total_accuracy, 3))
