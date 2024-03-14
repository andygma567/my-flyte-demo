# My Flyte + Runpod + Mlflow Demo

This repository contains the code for a Flyte enabled project using Python and [flytekit](https://docs.flyte.org/projects/flytekit/en/latest/).

## Structure

The repository is structured as follows:

- `hello-world/`: Contains a simple hello world application with a Dockerfile, Kubernetes configuration, and associated tests.
- `mlflow-ngrok-image/`: Contains the Dockerfile and Kubernetes configuration for the MLFlow tracking server.
- `my_project/`: Contains the Flyte workflows for the project.
- `my-flyte-images/`: Contains the Dockerfile and Kubernetes configuration for the Flyte images.

## Getting Started

To get up and running with your Flyte project, we recommend following the [Flyte getting started guide](https://docs.flyte.org/en/latest/getting_started.html).

## Building and Running

Each directory contains a `Dockerfile` for building the associated Docker image, and a `skaffold.yaml` for deploying the application with Skaffold.

## Testing

Tests for the hello world application can be found in `hello-world/test_hello_world.py`.

## License

This project is licensed under the terms of the license found in [my_project/LICENSE](my_project/LICENSE).
