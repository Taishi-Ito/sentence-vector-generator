from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_generate_status():
  response = client.post(
    "/generate",
    json={"text": "感動してみんなで泣ける映画"}
  )
  assert response.status_code == 200

def test_generate_response():
  response = client.post(
    "/generate",
    json={"text": "感動してみんなで泣ける映画"}
  )
  assert len(json.loads(response.json()["encoded_text"])) == 768

def test_generate_response_type01():
  response = client.post(
    "/generate",
    json={"text": "感動してみんなで泣ける映画"}
  )
  assert type(json.loads(response.json()["encoded_text"])[0]) == float

def test_generate_response_type02():
  response = client.post(
    "/generate",
    json={"text": "感動してみんなで泣ける映画"}
  )
  assert type(response.json()) == dict

def test_generate_validation_01():
  response = client.post(
    "/generate",
    json={"text": ""}
  )
  assert response.json() == {
    "detail":[
      {
        "loc":["body","text"],
        "msg":"ensure this value has at least 1 characters",
        "type":"value_error.any_str.min_length",
        "ctx":{"limit_value":1}
        }
      ]
    }

def test_generate_validation_02():
  response = client.post(
    "/generate",
    json={"texts": "感動してみんなで泣ける映画"}
  )
  assert response.json() == {
    "detail":[
      {
        "loc":["body","text"],
        "msg":"field required",
        "type":"value_error.missing"
        }
      ]
    }
