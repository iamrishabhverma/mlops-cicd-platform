# from prometheus_client import Counter, Histogram

# REQUEST_COUNT = Counter("ml_requests_total", "Total ML requests")
# REQUEST_LATENCY = Histogram("ml_request_latency_seconds", "ML request latency")


# metrics.py
from prometheus_client import Counter, Histogram, Gauge

# Count of prediction requests (success/error)
REQUEST_COUNT = Counter(
    "predict_requests_total",
    "Total prediction requests",
    ["status"]
)

# Prediction latency histogram
REQUEST_LATENCY = Histogram(
    "predict_request_latency_seconds",
    "Prediction latency"
)

# Distribution of delivery delay risk scores
PREDICTION_SCORE = Histogram(
    "delivery_delay_risk_score",
    "Distribution of delivery delay risk scores"
)

# Random Forest ensemble variance (uncertainty)
PREDICTION_VARIANCE = Gauge(
    "prediction_variance",
    "Random Forest ensemble variance"
)
