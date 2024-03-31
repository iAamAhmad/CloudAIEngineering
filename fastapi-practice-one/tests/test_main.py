from fastapi.testclient import TestClient
from fastapi_practice_one.main import app

def test_root_path():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

def test_piaic_root():
    client = TestClient(app)
    response = client.get("/home/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, where have you been so far?"}

def test_khan_root():
    client = TestClient(app)
    response = client.get("/about/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, where have you been so far? Tell me something about You!!!"}
