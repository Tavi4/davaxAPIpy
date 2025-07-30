function getApiKey() {
    const key = document.getElementById("apiKeyInput").value;
    if (!key) {
        alert("Please enter your API key first.");
        return null;
    }
    return key;
}

async function loadLogs() {
    const res = await fetch("/logs?limit=10");
    const data = await res.json();  // ✅ <-- THIS was likely missing

    console.log("Fetched logs:", data);

    const logsList = document.getElementById("logsList");
    logsList.innerHTML = "";

    data.logs.forEach(log => {
        const li = document.createElement("li");
        li.textContent = log;
        logsList.appendChild(li);
    });
}



async function callPow() {
    const key = getApiKey();
    if (!key) return;

    const base = document.getElementById("powBase").value;
    const exp = document.getElementById("powExp").value;
    const res = await fetch(`/pow?base=${base}&exponent=${exp}`, {
        headers: { "X-API-Key": key }
    });
    const data = await res.json();
    document.getElementById("powResult").innerText =
        data.result !== undefined ? "Result: " + data.result : "Error: " + (data.detail || "Unknown error");

    loadLogs();
}

async function callFactorial() {
    const key = getApiKey();
    if (!key) return;

    const n = document.getElementById("factN").value;
    const res = await fetch(`/factorial?n=${n}`, {
        headers: { "X-API-Key": key }
    });
    const data = await res.json();
    document.getElementById("factResult").innerText =
        data.result !== undefined ? "Result: " + data.result : "Error: " + (data.detail || "Unknown error");
    
    loadLogs();

}

async function callFibonacci() {
    const key = getApiKey();
    if (!key) return;

    const n = document.getElementById("fibN").value;
    const res = await fetch(`/fibonacci?n=${n}`, {
        headers: { "X-API-Key": key }
    });
    const data = await res.json();
    document.getElementById("fibResult").innerText =
        data.result !== undefined ? "Result: " + data.result : "Error: " + (data.detail || "Unknown error");

    loadLogs();
}
