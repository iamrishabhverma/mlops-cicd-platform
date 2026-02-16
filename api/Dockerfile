FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY app.py metrics.py ./
# COPY model/model.pkl ./model.pkl



COPY model ./model
COPY app.py metrics.py ./



EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

