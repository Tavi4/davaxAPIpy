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
