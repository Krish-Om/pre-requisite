from fastapi.testclient import TestClient

from src.app import HeroResponse, app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_hero_by_id():
    response = client.get("/heroes/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Flash"}
    assert isinstance(response.json(), dict) and HeroResponse(**response.json())


def test_get_all_heroes():
    response = client.get("/heroes")
    assert response.status_code == 200
    assert response.json() == [{"name": "Flash", "id": 1}, {"name": "Batman", "id": 2}]
    assert isinstance(response.json(), (list, dict))
