import os
import mlflow

# These environment variables are set by the Flyte workflow
# when it runs
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
execution_id_name = os.getenv("FLYTE_EXECUTION_ID")


def main():
    mlflow.set_tracking_uri(
        f"https://{username}:{password}@ostrich-comic-pup.ngrok-free.app"
    )
    mlflow.set_experiment("hello-world")
    name = os.getenv("NAME")
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
    with mlflow.start_run(run_name=execution_id_name):
        mlflow.log_param("name", name)
        mlflow.log_param("message", f"Hello, {name}!" if name else "Hello, World!")


if __name__ == "__main__":
    main()
