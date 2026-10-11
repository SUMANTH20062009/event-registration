from app import app

def test_home_page():
    app.testing = True
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Event Registration" in response.data

def test_registration():
    app.testing = True
    client = app.test_client()
    response = client.post("/", data={
        "name": "Test User",
        "email": "test@example.com",
        "event": "AI Seminar"
    })
    assert response.status_code == 200
    assert b"Test User" in response.data