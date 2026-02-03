# Cost-Aware Feature Optimization for Real-Time ML Systems

## Overview

In production machine learning systems, feature computation latency often dominates total inference time.
Adding more features can easily violate strict SLA constraints without providing proportional accuracy gains.

This project implements a **cost-aware feature optimization system** that automatically selects an optimal subset of features under a fixed latency budget, balancing **predictive value vs computational cost**.

The system is designed as an **internal ML engineering tool**, not a model showcase.

---

## Problem Statement

Real-time ML pipelines operate under hard constraints:

- Strict latency budgets (e.g. < 50 ms per request)
- Expensive stateful and windowed feature pipelines
- Trade-offs between system reliability and predictive performance

In such environments, the key question is:

> *Which features are worth computing when time is limited?*

This project answers that question using **measured latency**, **explicit constraints**, and **automated decision logic**.

---

## Dataset

- NYC Yellow Taxi Trip Records
- Event-based data containing timestamps, locations, and monetary values
- Well-suited for:
  - rolling window aggregations
  - stateful feature engineering
  - realistic latency profiling

Raw data is intentionally excluded from the repository.

---

## Feature Categories

| Feature Type | Description | Typical Latency |
|-------------|-------------|-----------------|
| Cheap features | Stateless scalar features | ~0.1 ms |
| Datetime features | Temporal derivations | ~20 ms |
| Windowed features | Rolling aggregations over time & location | 12–35 ms |

Windowed features introduce historical dependency, grouping, and state, making them significantly more expensive.

---

## System Architecture

Raw Data
↓
Feature Functions
↓
Latency Profiling
↓
Accuracy Estimation
↓
Cost-Aware Optimizer
↓
Selected Feature Set



Each component is isolated and independently testable.

---

## Methodology

1. Implemented multiple feature pipelines, including stateful rolling features
2. Measured real execution latency for each feature
3. Demonstrated cumulative latency violations under realistic budgets
4. Defined a non-leaky SLA violation prediction target
5. Built a latency-budget optimizer to prune features
6. Extended the optimizer to maximize accuracy gain per millisecond
7. Exposed decisions through a lightweight internal UI

---

## Latency Profiling Results

| Feature | Measured Latency (ms) |
|------|------------------------|
| rolling_trip_count | 34.05 |
| rolling_avg_duration | 13.10 |
| rolling_trip_fare_sum | 12.33 |

Even a small number of windowed features can exceed real-time SLA limits when combined.

---

## Optimization Strategy

Feature selection is performed using a value-density heuristic:

score = accuracy_gain / latency_cost


Features are selected greedily until the latency budget is exhausted.
This mirrors how production ML infrastructure teams reason about trade-offs.

---

## Example Optimization Output

**Latency Budget:** 40 ms

| Decision | Feature |
|--------|---------|
| Selected | rolling_avg_duration |
| Selected | rolling_trip_fare_sum |
| Dropped | rolling_trip_count |

**Total Latency:** 25.43 ms  
**Expected Accuracy Gain:** 0.075

Expensive, low-value features are automatically rejected.

---

## Internal Tooling Interface

A minimal Streamlit-based interface allows engineers to:

- Adjust latency budgets
- Observe feature selection decisions in real time
- Understand accuracy vs cost trade-offs interactively

The UI is intentionally lightweight and engineering-focused.

---

## Design Rationale

This project intentionally prioritizes **system constraints over model complexity**.

In real-time ML systems, optimizing feature pipelines often yields greater impact than tuning model architectures.
By making feature costs explicit and enforcing latency budgets, the system surfaces trade-offs that are typically implicit or ignored.

---

## Technologies Used

- Python
- pandas
- Rolling window feature engineering
- Latency profiling
- Constraint-based optimization
- Streamlit (internal tooling)

---

## Repository Structure

features/ # Feature computation logic
profiling/ # Latency measurement utilities
optimizer/ # Budget-aware feature selection
experiments/ # Data preparation and evaluation
ui/ # Lightweight internal interface



## Scope and Non-Goals

- No UI-heavy dashboards
- No deep learning without justification
- No price prediction or trading systems
- Focus on correctness, measurement, and system design

## UI SCREENSHOT
<img width="1578" height="837" alt="image" src="https://github.com/user-attachments/assets/b74062d7-8a6b-499f-b75b-73f74a287c01" />


