#!/bin/bash
echo "Container has been started"
export PYTHONUNBUFFERED=1

# sleep infinity

echo "Start mlflow server in the background"
mlflow server --host 0.0.0.0 --port 5000 &

echo "Start ngrok"
ngrok http 5000 --domain ostrich-comic-pup.ngrok-free.app --basic-auth "<USERNAME>:<PASSWORD>"