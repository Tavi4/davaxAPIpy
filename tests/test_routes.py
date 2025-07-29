from fastapi.testclient import TestClient
from math_service.core.main import app  # Adjust this import path if needed

client = TestClient(app)


# ───────────────────────
# ✅ /math/logs - LOGGING ENDPOINT TESTS
# ───────────────────────

def test_logs_endpoint():
    response = client.get("/math/logs?limit=5")
    assert response.status_code == 200
    assert "logs" in response.json()
    assert isinstance(response.json()["logs"], list)

def test_logs_filter_by_operation():
    response = client.get("/math/logs?operation=power&limit=3")
    assert response.status_code == 200
    logs = response.json()["logs"]
    assert all(log["operation"] == "power" for log in logs)


# ───────────────────────
# ✅ /math/logs - LOGGING ENDPOINT TESTS
# ───────────────────────

def test_logs_endpoint_returns_list():
    response = client.get("/math/logs?limit=5")
    assert response.status_code == 200
    logs = response.json().get("logs", [])
    assert isinstance(logs, list)

def test_logs_limit():
    response = client.get("/math/logs?limit=3")
    assert response.status_code == 200
    logs = response.json()["logs"]
    assert len(logs) <= 3

def test_logs_filter_by_operation():
    # Assumes at least one 'factorial' operation has been logged
    response = client.get("/math/logs?operation=factorial&limit=5")
    assert response.status_code == 200
    logs = response.json()["logs"]
    assert all(log["operation"] == "factorial" for log in logs)

def test_logs_empty_result():
    response = client.get("/math/logs?operation=nonexistent&limit=5")
    assert response.status_code == 200
    assert response.json()["logs"] == []
