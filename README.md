# Kubernetes Production Simulation Platform

Local Kubernetes environment simulating production-grade deployment workflows. Demonstrates rolling updates, rollbacks, multi-environment namespaces, and health checks using k3d.

## Architecture

```
k3d Local Cluster
        │
        ├── Namespace: dev
        │       └── k8s-app Deployment (2 replicas)
        │               └── Service (ClusterIP)
        │
        ├── Namespace: staging
        │
        └── Namespace: prod
```

## Features
- Multi-environment namespaces (dev/staging/prod)
- Rolling updates with zero downtime
- Automatic rollback on failure
- Readiness and liveness health probes
- Resource limits and requests
- Load balancing across replicas

## Tech Stack
- **Kubernetes (k3d)** - Local K8s cluster
- **kubectl** - Cluster management
- **FastAPI** - Demo microservice
- **Docker** - Container images

## Rolling Update Demo

```bash
# Deploy version 1.0.0
kubectl apply -f k8s/deployment.yml

# Update to version 2.0.0
kubectl set image deployment/k8s-app k8s-app=k8s-app:2.0.0 -n dev
kubectl rollout status deployment/k8s-app -n dev

# Rollback to previous version
kubectl rollout undo deployment/k8s-app -n dev
```

## Quick Start

```bash
# Install k3d
winget install k3d  # Windows
brew install k3d    # Mac

# Create cluster
k3d cluster create k8s-platform

# Deploy application
kubectl apply -f k8s/namespace.yml
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml

# Access application
kubectl port-forward -n dev svc/k8s-app 8000:80
```

Open http://localhost:8000

## Kubernetes Manifests

| File | Description |
|------|-------------|
| k8s/namespace.yml | dev, staging, prod namespaces |
| k8s/deployment.yml | App deployment with health checks |
| k8s/service.yml | ClusterIP service |

## Cost
$0 - Runs entirely on local k3d cluster
