# MLOps CI/CD Platform

FastAPI + Docker + K8s + GitHub Actions + Prometheus + Grafana + Slack

## Quick Start

Recommended: build from the repository root so the Docker build context includes both `api/` and `model/`.

1. Train the model locally (creates `model/model.pkl`):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r api/requirements.txt
python model/train.py
```

2. Build the Docker image (from repo root):

```bash
# replace `iamrishabhverma` with your Docker Hub username if pushing later
docker build -t iamrishabhverma/ml-api:latest -f api/Dockerfile .
```

If you encounter an error like:
```
ERROR: failed to build: failed to solve: failed to compute cache key: failed to calculate checksum of ref ...: "/requirements.txt": not found
```
This usually indicates you built the image from the `api/` context or changed the Dockerfile paths. To fix:
- Build from the repository root, not the `api/` folder. Use `docker build -f api/Dockerfile .`.
- Or change `api/Dockerfile` to use `api/requirements.txt` and `model/model.pkl` (this repo already uses explicit paths).

3. Run the Docker image locally:

```bash
docker run --rm -p 8000:8000 iamrishabhverma/ml-api:latest
```

4. Test the API:

```bash
curl http://localhost:8000/
curl "http://localhost:8000/predict?x=5"
curl http://localhost:8000/metrics
```

For Kubernetes/k3d deployment, follow the k3d steps documented in the repo's `k8s/` and `k3d/` folders.

### k3d local cluster
Use the `k3d` config in `k3d/cluster.yaml` to create a local cluster:

```bash
# Create the cluster from the repo root
k3d cluster create --config k3d/cluster.yaml
```

If you see an error like `Schema Validation failed ... Additional property name is not allowed`, it likely means the cluster YAML has `name` at the top-level instead of nested under `metadata`. In this repo the YAML has been updated to use `metadata.name: mlops`. Re-run the command after pulling the latest copy.

If you see an error like `failed to transform ports: error parsing port spec '8080:80@loadbalancer'`, your installed version of `k3d` might not support `@loadbalancer` node selectors. The simplest fix is to remove the `@loadbalancer` suffix and use a plain `hostPort:containerPort` mapping (this repo sets `ports: - port: 8080:80` for compatibility):

```bash
# This cluster config uses a simple host-to-container port mapping for broad compatibility
k3d cluster create --config k3d/cluster.yaml
```

Check the cluster:

```bash
k3d cluster list
kubectl get nodes
```

