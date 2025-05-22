from app import app

def test_hello():
    client = app.test.client()
    response = client.get("?hello")
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Ivanti!"}