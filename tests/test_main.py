from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI application running"}


def test_about():
    response = client.get("/about")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Docker and GitHub Actions learning project"
    }

def test_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["name"] == "Laptop"