import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))




import streamlit as st
from optimizer.feature_registry import FEATURES

st.set_page_config(page_title="Cost-Aware Feature Optimizer", layout="centered")

st.title("Cost-Aware Feature Optimizer")
st.caption("Select features under a strict latency budget")

latency_budget = st.slider(
    "Latency Budget (ms)",
    min_value=10.0,
    max_value=80.0,
    value=40.0,
    step=5.0
)

selected = []
dropped = []
total_latency = 0.0
total_accuracy = 0.0

def score(item):
    name, meta = item
    return meta["accuracy_gain"] / meta["latency_ms"]

for name, meta in sorted(FEATURES.items(), key=score, reverse=True):
    if total_latency + meta["latency_ms"] <= latency_budget:
        selected.append(name)
        total_latency += meta["latency_ms"]
        total_accuracy += meta["accuracy_gain"]
    else:
        dropped.append(name)

st.subheader("Selected Features")
st.success(selected)

st.subheader("Dropped Features")
st.error(dropped)

st.markdown("---")
st.write("**Total Latency:**", round(total_latency, 2), "ms")
st.write("**Expected Accuracy Gain:**", round(total_accuracy, 3))
