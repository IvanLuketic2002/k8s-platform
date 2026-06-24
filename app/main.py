from fastapi import FastAPI
import os
import socket

app = FastAPI(title="K8s Microservice")

@app.get("/")
def root():
    return {
        "message": "Hello from Kubernetes!",
        "version": os.getenv("APP_VERSION", "2.0.0"),
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "dev")
    }

@app.get("/health")
def health():
    return {"status": "ok"}
