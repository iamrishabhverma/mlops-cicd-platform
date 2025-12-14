from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter("ml_requests_total", "Total ML requests")
REQUEST_LATENCY = Histogram("ml_request_latency_seconds", "ML request latency")
