## Day 1 – Feature Cost Measurement

Implemented baseline feature pipelines and measured real execution latency (mean and p95) on NYC taxi data. Established clean project structure and resolved Python packaging and dependency issues to enable reproducible profiling.


Feature                  Cost (ms)     Accuracy
------------------------------------------------
trip_distance             ~0.2         0.825
trip_duration_minutes     ~20          0.999
both                       ~20.2        1.00
