#!/bin/bash

set -e

echo "🚀 Starting Kubernetes port-forwarding..."

# Function to clean up background processes on exit
cleanup() {
  echo ""
  echo "🛑 Stopping port-forwarding..."
  kill $(jobs -p) 2>/dev/null || true
  exit 0
}

trap cleanup SIGINT SIGTERM

# Port forward commands
kubectl port-forward svc/ml-api-service 8000:80 -n mlops &
echo "✅ ml-api-service → http://localhost:8000"

kubectl port-forward svc/prometheus 9090:9090 -n mlops &
echo "✅ Prometheus → http://localhost:9090"

kubectl port-forward svc/grafana 3000:3000 -n mlops &
echo "✅ Grafana → http://localhost:3000"

kubectl port-forward svc/argocd-server -n argocd 8080:443 &
echo "✅ ArgoCD → https://localhost:8080"

echo ""
echo "🎯 All services are port-forwarded."
echo "Press CTRL+C to stop."

# Wait indefinitely
wait
