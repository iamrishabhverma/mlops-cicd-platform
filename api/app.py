import logging
import os
from fastapi import FastAPI
import pickle, time
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from pydantic import BaseModel

try:
    from metrics import REQUEST_COUNT, REQUEST_LATENCY, ETA_HISTOGRAM
except ImportError:
    REQUEST_COUNT = REQUEST_LATENCY = ETA_HISTOGRAM = None

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "model.pkl")


print("Looking for model at:", MODEL_PATH)
print("Exists?", os.path.exists(MODEL_PATH))

# Load the model
try:
    model = pickle.load(open(MODEL_PATH, "rb"))
    print("Loaded model successfully")
except Exception as e:
    print(f"Failed to load model: {e}")
    raise  

# Pydantic schema for prediction
class PredictionRequest(BaseModel):
    distance: float
    weight: float
    speed: float
    traffic: float
    weather: float

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/predict")
def predict(data: PredictionRequest):
    start = time.time()

    features = [[
        data.distance,
        data.weight,
        data.speed,
        data.traffic,
        data.weather
    ]]

    result = model.predict(features)[0]

    # Metrics logging
    if REQUEST_LATENCY:
        REQUEST_LATENCY.observe(time.time() - start)
    if REQUEST_COUNT:
        REQUEST_COUNT.labels(status="success").inc()
    if ETA_HISTOGRAM:
        ETA_HISTOGRAM.observe(result)

    # Log prediction
    logger.info({
        "distance": data.distance,
        "weight": data.weight,
        "speed": data.speed,
        "traffic": data.traffic,
        "weather": data.weather,
        "prediction": float(result)
    })

    return {
        "eta_hours": round(result, 2)
    }
