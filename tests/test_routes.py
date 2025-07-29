from fastapi.testclient import TestClient
from math_service.core.main import app

client = TestClient(app)


# /math/pow

def test_pow():
    response = client.get("/math/pow?base=2&exponent=3")
    assert response.status_code == 200
    assert response.json()["result"] == 8

def test_pow_zero_zero():
    response = client.get("/math/pow?base=0&exponent=0")
    assert response.status_code == 200
    assert response.json()["result"] == 1

def test_pow_negative_base():
    response = client.get("/math/pow?base=-2&exponent=3")
    assert response.status_code == 200
    assert response.json()["result"] == -8

def test_pow_negative_exponent():
    response = client.get("/math/pow?base=2&exponent=-3")
    assert response.status_code == 200
    assert round(response.json()["result"], 6) == 0.125

def test_pow_missing_param():
    response = client.get("/math/pow?base=2")
    assert response.status_code == 422

# /math/factorial

def test_factorial():
    response = client.get("/math/factorial?n=5")
    assert response.status_code == 200
    assert response.json()["result"] == 120

def test_factorial_zero():
    response = client.get("/math/factorial?n=0")
    assert response.status_code == 200
    assert response.json()["result"] == 1

def test_factorial_one():
    response = client.get("/math/factorial?n=1")
    assert response.status_code == 200
    assert response.json()["result"] == 1

def test_negative_factorial():
    response = client.get("/math/factorial?n=-5")
    assert response.status_code == 422

def test_large_factorial():
    response = client.get("/math/factorial?n=10000")
    assert response.status_code in (422, 400)


# /math/fibonacci

def test_fibonacci():
    response = client.get("/math/fibonacci?n=7")
    assert response.status_code == 200
    assert response.json()["result"] == 13

def test_fibonacci_zero():
    response = client.get("/math/fibonacci?n=0")
    assert response.status_code == 200
    assert response.json()["result"] == 0

def test_fibonacci_one():
    response = client.get("/math/fibonacci?n=1")
    assert response.status_code == 200
    assert response.json()["result"] == 1

def test_large_fibonacci():
    response = client.get("/math/fibonacci?n=10001")
    assert response.status_code in (422, 400, 500)
