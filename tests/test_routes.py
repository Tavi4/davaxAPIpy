from fastapi.testclient import TestClient
from math_service.core.main import app

client = TestClient(app)


#  /math/logs - LOGGING ENDPOINT TESTS


def test_logs_endpoint():
    response = client.get("/logs?limit=5")
    assert response.status_code == 200
    assert "logs" in response.json()
    assert isinstance(response.json()["logs"], list)


def test_logs_limit():
    response = client.get("/logs?limit=3")
    assert response.status_code == 200
    logs = response.json()["logs"]
    assert len(logs) <= 3


def test_logs_filter_by_operation():
    # Assumes at least one 'factorial' operation has been logged
    response = client.get("/logs?operation=factorial&limit=5")
    assert response.status_code == 200
    logs = response.json()["logs"]
    assert all(log["operation"] == "factorial" for log in logs)


def test_logs_empty_result():
    response = client.get("/logs?operation=nonexistent&limit=5")
    assert response.status_code == 200
    assert response.json()["logs"] == []

# /math/pow

def test_pow():
    response = client.get("/pow?base=2&exponent=3")
    assert response.status_code == 200
    assert response.json()["result"] == 8

def test_pow_zero_zero():
    response = client.get("/pow?base=0&exponent=0")
    assert response.status_code == 200
    assert response.json()["result"] == 1

def test_pow_negative_base():
    response = client.get("/pow?base=-2&exponent=3")
    assert response.status_code == 200
    assert response.json()["result"] == -8

def test_pow_negative_exponent():
    response = client.get("/pow?base=2&exponent=-3")
    assert response.status_code == 200
    assert round(response.json()["result"], 6) == 0.125

def test_pow_missing_param():
    response = client.get("/pow?base=2")
    assert response.status_code == 422

# /math/factorial

def test_factorial():
    response = client.get("/factorial?n=5", headers={"X-API-Key": "secret"})
    assert response.status_code == 200
    assert response.json()["result"] == 120

def test_factorial_zero():
    response = client.get("/factorial?n=0", headers={"X-API-Key": "secret"})
    assert response.status_code == 200
    assert response.json()["result"] == 1

def test_factorial_one():
    response = client.get("/factorial?n=1", headers={"X-API-Key": "secret"})
    assert response.status_code == 200
    assert response.json()["result"] == 1

def test_negative_factorial():
    response = client.get("/factorial?n=-5")
    assert response.status_code == 422

def test_large_factorial():
    response = client.get("/factorial?n=10000")
    assert response.status_code in (422, 400)


# /math/fibonacci

def test_fibonacci():
    response = client.get("/fibonacci?n=7", headers={"X-API-Key": "secret"})
    assert response.status_code == 200
    assert response.json()["result"] == 8

def test_fibonacci_zero():
    response = client.get("/fibonacci?n=0", headers={"X-API-Key": "secret"})
    assert response.status_code == 200
    assert response.json()["result"] == 0

def test_fibonacci_one():
    response = client.get("/fibonacci?n=1", headers={"X-API-Key": "secret"})
    assert response.status_code == 200
    assert response.json()["result"] == 1

def test_large_fibonacci():
    response = client.get("/fibonacci?n=10001")
    assert response.status_code in (422, 400, 500)

