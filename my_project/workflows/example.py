"""A basic Flyte project template"""

import flytekit
from flytekit import task, workflow
import runpod
from pprint import pformat
import os


@task(container_image="pipelinepilot/flyte-task")
def trigger_runpod(api_key: str) -> str:
    """A simple Flyte task to say "Hello".

    The @task decorator allows Flyte to use this function as a Flyte task,
    which is executed as an isolated, containerized unit of compute.
    """
    # Get the flyte execution id in order to use it as a unique name for the
    # mlflow run
    execution_id_name = flytekit.current_context().execution_id.name
    print(f"execution_id_name: {execution_id_name}")

    # Create a run pod instance
    runpod.api_key = api_key
    print("creating pod")
    runpod.create_pod(
        name="test-pod",
        image_name="pipelinepilot/hello-world-amd64",
        gpu_type_id="NVIDIA GeForce RTX 3070",
        env={
            "NAME": "Tran",
            "USERNAME": "<USERNAME>",
            "PASSWORD": "<PASSWORD>",
            "FLYTE_EXECUTION_ID": f"{execution_id_name}",
        },
    )

    # Get all my pods
    pods = runpod.get_pods()
    pods_str = pformat(pods)

    return pods_str


@workflow
def wf(api_key: str = os.environ.get("API_KEY")) -> str:
    """Declare workflow called `wf`.

    The @workflow decorator defines an execution graph that is composed of
    tasks and potentially sub-workflows. In this simple example, the workflow
    is composed of just one task.

    There are a few important things to note about workflows:
    - Workflows are a domain-specific language (DSL) for creating execution
      graphs and therefore only support a subset of Python's behavior.
    - Tasks must be invoked with keyword arguments
    - The output variables of tasks are Promises, which are placeholders for
      values that are yet to be materialized, not the actual values.
    """
    # greeting = say_hello(name=name)
    pods_str = trigger_runpod(api_key=api_key)
    return pods_str


if __name__ == "__main__":
    # Execute the workflow by invoking it like a python
    # function and passing in the necessary parameters
    API_KEY = os.environ.get("API_KEY")
    print(f"Running wf() {wf(api_key=API_KEY)}")
