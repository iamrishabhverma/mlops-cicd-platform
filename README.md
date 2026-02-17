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

# Screen shots
<img width="2864" height="1516" alt="Screenshot 2026-02-16 at 8 12 49 PM" src="https://github.com/user-attachments/assets/82835abe-5feb-4b01-9a08-1dcac1350ad2" />

<img width="1426" height="753" alt="Screenshot 2026-02-16 at 4 10 36 PM" src="https://github.com/user-attachments/assets/bde34c53-65b0-4eff-98d7-46505989ebbd" />


<img width="2834" height="1508" alt="Screenshot 2026-02-16 at 6 57 44 PM" src="https://github.com/user-attachments/assets/17cfbf41-692a-4243-b9bd-1a0e5b9bcc4f" />


<img width="2834" height="1508" alt="Screenshot 2026-02-16 at 7 00 09 PM" src="https://github.com/user-attachments/assets/724773d6-d097-4608-8f23-d81d479c8825" />


<img width="2834" height="1508" alt="Screenshot 2026-02-16 at 7 43 22 PM" src="https://github.com/user-attachments/assets/77b5d3b6-6576-4a52-a688-3f88ba181314" />
<img width="2834" height="1508" alt="Screenshot 2026-02-16 at 7 44 25 PM" src="https://github.com/user-attachments/assets/0fdfd1c8-3776-4135-a16f-850df4242666" />


<img width="1912" height="930" alt="Screenshot 2026-02-16 at 7 57 18 PM" src="https://github.com/user-attachments/assets/3a7eb53a-d1ae-4f5a-bb63-6c95defe8008" />



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

### Make sure argoCD is installed via manifest
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### Verfify ArgoCD AutoSync 
```bash
kubectl get pods -n argocd
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

### Verify Context
```bash
argocd context
argocd version  
  ```

### If Prometheus is not installed, install it via Helm

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
kubectl create namespace monitoring
helm install prometheus prometheus-community/prometheus \
  -n monitoring
```


### Run Bash script
```bash
chmod +x deploy.sh
./deploy.sh
```

### Port-forwarding, for FastAPI(8000), Prometheus(9000), Grafana(3000), ArgoCD(8080)
```bash
./forward.sh
```
### OR 

```bash
kubectl port-forward svc/ml-api-service 8000:80 -n mlops
kubectl port-forward svc/prometheus 9090:9090 -n mlops
kubectl port-forward svc/grafana 3000:3000 -n mlops
kubectl port-forward svc/argocd-server -n argocd 8080:443 #ArgoCD UI
```













