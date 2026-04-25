import json
from app import app

def test_add_api():
    client = app.test_client()

    response = client.post("/add",
        data=json.dumps({"a": 5, "b": 5}),
        content_type='application/json')

    assert response.status_code == 200
    assert response.json["result"] == 10

def test_missing_data():
    client = app.test_client()

    response = client.post("/add",
        data=json.dumps({"a": 5}),
        content_type='application/json')

    assert response.status_code == 400
