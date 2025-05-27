import requests
from threading import Thread
from src import server


def test_connect_with_one_user():
    server_thread = Thread(target=server.create_server, args=("127.0.0.1", 8080))
    server_thread.start()
    response = requests.get("http://127.0.0.1:8080")
    assert response.status_code == 200


def test_connect_with_multiple_users():
    for _ in range(5):
        response = requests.get("http://127.0.0.1:8080")
        assert response.status_code == 200
