import mlflow
from hello_world import main
import os
from mlflow.client import MlflowClient


def test_experiment_is_created(monkeypatch, tmp_path):
    # This is the test function
    # It monkey patches mlflow.set_tracking_uri()

    # Define a new function that calls mlflow.set_tracking_uri(tmpdir)
    def mock_set_tracking_uri(uri):
        os.environ["MLFLOW_TRACKING_URI"] = str(tmp_path)

    # Use monkeypatch to replace mlflow.set_tracking_uri with the new function
    monkeypatch.setattr(mlflow, "set_tracking_uri", mock_set_tracking_uri)

    # Now when you call main(), it will use the new function
    main()

    client = MlflowClient(tracking_uri=str(tmp_path))
    experiment = client.get_experiment_by_name("hello-world")
    assert experiment is not None


def test_name_is_logged(monkeypatch, tmp_path):
    # This is the test function
    # It monkey patches mlflow.set_tracking_uri()

    # Define a new function that calls mlflow.set_tracking_uri(tmpdir)
    def mock_set_tracking_uri(uri):
        os.environ["MLFLOW_TRACKING_URI"] = str(tmp_path)

    # Use monkeypatch to replace mlflow.set_tracking_uri with the new function
    monkeypatch.setattr(mlflow, "set_tracking_uri", mock_set_tracking_uri)

    # Now when you call main(), it will use the new function
    main()

    client = MlflowClient(tracking_uri=str(tmp_path))
    experiment = client.get_experiment_by_name("hello-world")
    latest_run = client.search_runs(
        experiment.experiment_id, max_results=1
    )[0]
    assert "name" in latest_run.data.params
    assert "message" in latest_run.data.params
