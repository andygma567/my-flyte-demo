#!/bin/bash
echo "Container has been started"
export PYTHONUNBUFFERED=1

echo "Run the python script"
python hello_world.py

echo "Stop the pod after the script has finished"
if [[ -n $RUNPOD_POD_ID ]]; then
    echo "Stopping the pod"
    runpodctl remove pod $RUNPOD_POD_ID
    # runpodctl stop pod $RUNPOD_POD_ID
else
    echo "Running in standalone mode"
    sleep infinity
fi
