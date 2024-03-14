import requests
from requests.auth import HTTPBasicAuth


def test_mlflow_server_connection():
    url = "https://ostrich-comic-pup.ngrok-free.app"
    response = requests.get(url, auth=HTTPBasicAuth("<USERNAME>", "<PASSWORD>"))
    assert response.status_code == 200


def test_mlflow_server_connection_without_auth():
    url = "https://ostrich-comic-pup.ngrok-free.app"
    response = requests.get(url)
    assert response.status_code == 401
