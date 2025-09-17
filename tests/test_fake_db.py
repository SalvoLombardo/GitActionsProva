import pytest
from app import create_app

@pytest.fixture
def client():
    app=create_app()
    app.config["TESTING"]=True
    with app.test_client() as client:
        yield client

def test_primo(client, monkeypatch):
    def fake_query():
        return {'id':1, "nome": "Mario"}
    monkeypatch.setattr("app.models.get_primo",fake_query)

    response= client.get("/primo")
    assert response.status_code==200
    assert response.json== {'id':1, "nome": "Mario"}

def test_secondo(client, monkeypatch):
    def fake_query():
        return {'id':2, "nome": "Paolo"}
    monkeypatch.setattr("app.models.get_primo",fake_query)

    response= client.get("/primo")
    assert response.status_code==200
    assert response.json== {'id':2, "nome": "Paolo"}