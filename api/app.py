from fastapi import FastAPI
import pickle, time
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from metrics import REQUEST_COUNT, REQUEST_LATENCY

app = FastAPI()
model = pickle.load(open("/app/model.pkl", "rb"))

@app.get("/")
def health():
    return {"status": "running"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/predict")
def predict(x: float):
    start = time.time()
    result = x * 2   # prediction logic
    REQUEST_LATENCY.observe(time.time() - start)
    REQUEST_COUNT.inc()
    return {"prediction": result}