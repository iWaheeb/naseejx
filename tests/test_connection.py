import requests

def test_connect_with_one_user():
    response = requests.get("http://127.0.0.1:8080")
    assert response.status_code == 200

def test_connect_with_multiple_users():
    for _ in range(5):
        response = requests.get("http://127.0.0.1:8080")
        assert response.status_code == 200
