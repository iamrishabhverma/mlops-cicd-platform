# MLOps Continuous Integration & Continuous Deployment (CI/CD) Platform
### Automated Logistics ETA Prediction Pipeline with GitOps Engine & Kubernetes Orchestration
**Rishabh Verma** | [github.com/iamrishabhverma](https://github.com/iamrishabhverma) | [linkedin.com/in/iamrishabhverma](https://www.linkedin.com/in/iamrishabhverma)

---

## Project Overview
This platform delivers an enterprise-grade, GitOps-driven MLOps CI/CD infrastructure that automates the complete lifecycle of a **Random Forest Regressor (`RandomForestRegressor`)** model trained to predict **ETA (Estimated Time of Arrival)** for logistics freight operations. By treating both machine learning assets and cluster configurations as declarative software code, this architecture ensures deterministic, zero-downtime model deployments alongside live tracking monitoring.

The system completely abstracts manual operations by enforcing a distinct division of labor between two core orchestration components:
1. **Continuous Integration Pipeline (GitHub Actions):** Automates linting, structural testing, training, validation threshold gating, and immutable packaging.
2. **Continuous Delivery Pipeline (ArgoCD & Kubernetes):** Employs a declarative GitOps engine to reconcile cluster state, execute canary/blue-green rolling microservice updates, and establish automated metrics scrape points.

---

## Key Achievements
* **Automated ETA Regression Model:** Engineered an automated training pipeline utilizing `RandomForestRegressor` to compute highly accurate trip time estimates based on haul distances, payload dimensions, transit speed, and traffic conditions.
* **Automated Quality Performance Gates:** Implemented metric evaluation boundaries during the CI phase to dynamically block containerization workflows unless the model meets strict baseline validation metrics.
* **Declarative GitOps Delivery Infrastructure:** Integrated ArgoCD to actively watch git state modifications (`k8s YAML`), eliminating configuration drift by automatically synchronizing desired production configurations onto the live environment.
* **Lightweight Local Cluster Topologies:** Standardized containerized runtime environments inside a highly efficient **Kubernetes (k3d / k3s)** local cluster setup to replicate enterprise-level cloud behaviors smoothly.
* **Real-time Observability Core:** Wired automated telemetry collection channels using **Prometheus** to pull analytics straight from `/metrics` endpoints, feeding a live **Grafana** visualization grid for active performance auditing.
* **Enterprise Notification Channels:** Linked asynchronous webhooks connecting pipeline execution phases directly to team messaging applications (`Slack: #all-devops-clan`) to ensure real-time status transparency.

---

## Complete Pipeline Architecture & Data Flow
<img width="480" height="720" alt="image" src="https://github.com/user-attachments/assets/44c3107e-3bb9-4960-b84f-26028706ba79" />


### Detailed Lifecycle Execution Steps:
1. **The Code Trigger:** A developer pushes code adjustments or fresh telemetry training sets to the remote repository `main` branch.
2. **Continuous Integration Run:** GitHub Actions catches the change event, immediately starting tasks to initialize training arrays, compile structural weights via `src/train.py`, test precision bounds, and construct a clean container package. Status webhooks push execution reports directly onto dedicated communication lines (`#all-devops-clan`).
3. **Registry Storage:** Validated application layers are wrapped as an optimized, immutable image target, marked with appropriate semantic metadata, and sent up directly to **Docker Hub** as `ml-api:latest`.
4. **GitOps State Verification:** ArgoCD constantly evaluates current deployment manifestations across the live Kubernetes clusters against target properties mapped in version control. When a change in manifest versions or deployment state occurs, it triggers zero-downtime application rollouts.
5. **Runtime Cluster Isolation:** The serving microservice drops inside standard **Kubernetes (k3d / k3s)** namespaces as an optimized **FastAPI** deployment endpoint.
6. **Telemetry Scrape Tracking:** Prometheus queries the internal pods via `/metrics` regularly, logging data queries and performance profiles, which are displayed on live monitoring panels in Grafana.

---

## Production Deployment & Platform Interfaces

### 1. Interactive API Serving Interface (FastAPI)
The deployed machine learning microservice exposes dedicated endpoints for live system performance auditing (`/metrics`), cluster deployment verification (`/health`), and programmatic ETA evaluations (`/predict`).

<img width="2864" height="1516" alt="550687594-82835abe-5feb-4b01-9a08-1dcac1350ad2" src="https://github.com/user-attachments/assets/718d2ec8-877e-4932-9a4b-37c8e9e70380" />


### 2. Live Evaluation Live Testing Output
Sending automated validation JSON requests mapping distance, payload weight, transit speed, and environmental indices returns low-latency inference payloads natively over HTTP.

<img width="1426" height="753" alt="550687098-bde34c53-65b0-4eff-98d7-46505989ebbd" src="https://github.com/user-attachments/assets/9681c410-fc12-47f7-9af6-19f7d3c7cb4c" />
<img width="2834" height="1508" alt="550687088-77b5d3b6-6576-4a52-a688-3f88ba181314" src="https://github.com/user-attachments/assets/be2fa697-4417-46be-90ad-c2b5472d0c37" />


### 3. Declarative GitOps Git Synchronization (ArgoCD Dashboard)
Our platform utilizes active ArgoCD loops to continuously poll for configuration updates inside the Git manifests repository, automatically reconciling live environments without requiring manual access to cluster consoles.

<img width="2834" height="1508" alt="550687097-17cfbf41-692a-4243-b9bd-1a0e5b9bcc4f" src="https://github.com/user-attachments/assets/7c1a5a74-306d-4f46-9946-f5f2fa16fae3" />


### 4. Telemetry Scraping & PromQL Inspection (Prometheus Engine)
A specialized `Prometheus-FastAPI-Instrumentator` core parses runtime telemetry details, cataloging memory profiles and CPU logs across internal namespaces via custom application hooks (`process_cpu_seconds_total`).

<img width="2834" height="1508" alt="550687084-0fdfd1c8-3776-4135-a16f-850df4242666" src="https://github.com/user-attachments/assets/510039a6-1883-4b08-bbfc-f399a266f1b1" />


### 5. Multi-Service Visual Performance Auditing (Grafana Framework)
To analyze deployment metrics effortlessly, Grafana links directly to raw Prometheus datastores, parsing time-series calculations into clear telemetry dashboards.

<img width="1912" height="930" alt="550687082-3a7eb53a-d1ae-4f5a-bb63-6c95defe8008" src="https://github.com/user-attachments/assets/b2b42318-9663-443a-b546-807813f91b88" />


### 6. Pipeline Notifications Channel (Slack Bot Integration)
GitHub CI pipelines and ArgoCD deployment systems push real-time status notifications straight onto corporate communication lines (`#all-devops-clan`), confirming compilation logs, commit IDs, and target branch state instantly.

<img width="2834" height="1508" alt="550687090-724773d6-d097-4608-8f23-d81d479c8825" src="https://github.com/user-attachments/assets/f6aaeafa-7ba0-42e7-9c72-33687880b549" />


### GitHub Actions Workflow

The deployment pipeline follows GitOps principles.

1. Developer pushes code.
2. GitHub Actions builds Docker image.
3. Image is pushed to Docker Hub.
4. Kubernetes manifests are updated.
5. ArgoCD detects repository changes.
6. ArgoCD synchronizes Kubernetes.
7. Rolling deployment occurs.
8. Prometheus begins scraping metrics.
9. Grafana dashboards update automatically.

<img width="2834" height="1508" alt="550687090-724773d6-d097-4608-8f23-d81d479c8825" src="Screenshot 2026-07-14 at 6.51.37 PM.png" />


---

## Technology Stack
* **ML Stack & Core Modeling:** Python 3, boto3, Scikit-Learn (`RandomForestRegressor`), Pandas
* **Serving Layer Microservice:** FastAPI, Uvicorn, Prometheus-FastAPI-Instrumentator
* **CI Validation Automation:** GitHub Actions
* **Container Registry & Management:** Docker, Docker Hub
* **GitOps Continuous Delivery:** ArgoCD
* **Container Orchestration Fabric:** Kubernetes (k3d / k3s engines)
* **Observability & Infrastructure Auditing:** Prometheus, Grafana
* **Team Communication Integrations:** Slack Webhooks

---


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













