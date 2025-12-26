#!/bin/bash

# Exit on error
set -e

echo "============================"
echo "PREREQUISITES:"
echo "============================"
python3 -m pip install --upgrade pip
python3 -m pip install scikit-learn



echo "============================"
echo "Step 1: Train the model"
echo "============================"
cd api/model
python3 train.py
cd ..
cd ..
echo "Model trained and saved to model/model.pkl"

echo "============================"
echo "Step 2: Create K3d cluster"            #Run one time only
echo "============================"
k3d cluster create --config k3d/cluster.yaml
echo "K3d cluster created"

echo "============================"
echo "Step 3: Build Docker image"
echo "============================"
cd api
docker build -t ml-api .
cd ..
echo "Docker image ml-api built successfully"

echo "============================"
echo "Step 4: Import Docker image into K3d cluster"
echo "============================"
k3d image import ml-api:latest -c mlops
echo "Image imported into K3d cluster"

echo "============================"
echo "Step 5: Deploy to Kubernetes cluster"
echo "============================"

kubectl apply -f k8s/ml-api/namespace.yaml  
kubectl apply -f k8s/ml-api/deployment.yaml
kubectl apply -f k8s/ml-api/service.yaml
kubectl apply -f ./k8s/monitoring/prometheus-service.yaml
kubectl apply -f ./k8s/monitoring/grafana-service.yaml
kubectl apply -f ./k8s/monitoring/grafana-deployment.yaml
kubectl get all -n mlops

echo "============================"
echo "Step 6: Verify deployment"
echo "============================"
kubectl get pods -n mlops
kubectl get svc -n mlops


echo "============================"
echo "Deployment script finished!"
echo "============================"

