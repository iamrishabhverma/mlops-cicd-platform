# MLOps CI/CD Platform

MLOps FastAPI ML API Pipeline using FastAPI + Docker + K8s + GitHub Actions + Prometheus + Grafana + Slack

This project demonstrates a production-ready MLOps pipeline for a machine learning model:

FastAPI ML API: Serves ML predictions and exposes metrics
Docker: Containerizes the application
Kubernetes (k3d): Orchestrates deployment
ArgoCD Gitops CD operations
Prometheus: Monitors metrics
GitHub Actions: Automates CI/CD pipeline
Slack notifications: Sends alerts on deployment


[mlops-Readme.pdf](https://github.com/user-attachments/files/24224828/mlops-Readme.pdf)



<img width="1024" height="1536" alt="CI_CD pipeline with Slack integration" src="https://github.com/user-attachments/assets/6339c249-239f-48c2-9ac6-6c2502649b4f" />


## Quick Start

## Step-by-Step Setup

### 1. Prerequisites
Make sure the following tools are installed:
```bash
docker --version
kubectl version --client
k3d version
helm version
```
### 2. Train the model
```bash
cd model
python train.py
cd ..
```
```bash
ls model/
```
train.py  model.pkl.   // make sure model.pkl is present
### 3. Create k3d cluster
```bash
k3d cluster create --config k3d/cluster.yaml
```
### Build docker image 
```bash
cd api
docker build -t ml-api .
```
### Import image in K3d cluster
```bash
k3d image import ml-api:latest -c mlops
```
### Deploy to k3s cluster
```bash 
kubectl apply -f k8s/ml-api/namespace.yaml  
kubectl apply -f k8s/ml-api/deployment.yaml
kubectl apply -f k8s/ml-api/service.yaml
kubectl apply -f argocd/mlops-app.yaml
kubectl apply -f ./k8s/monitoring/prometheus-service.yaml
kubectl apply -f ./k8s/monitoring/grafana-service.yaml
kubectl apply -f ./k8s/monitoring/grafana-deployment.yaml
kubectl get all -n mlops
```
### Verify deployment
```bash
kubectl get pods -n mlops
kubectl get svc -n mlops
```

### Verfify ArgoCD AutoSync 
```bash
kubectl get applications -n argocd
```

### Login ArgoCD
```bash
argocd login localhost:8080 \
  --username admin \
  --password $(kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d) \
  --insecure
```

# Verify Context
```bash
argocd context
argocd version  
  ```


### Port-forwarding, for FastAPI(8000), Prometheus(9000), Grafana(3000), ArgoCD(8080)
```bash
kubectl port-forward svc/ml-api-service 8000:80 -n mlops
kubectl port-forward svc/prometheus 9090:9090 -n mlops
kubectl port-forward svc/grafana 3000:3000 -n mlops
kubectl port-forward svc/argocd-server -n argocd 8080:443 #ArgoCD UI
```

### Run Bash script
```bash
chmod +x deploy.sh
./deploy.sh
```












