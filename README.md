# Math Microservice

A learning project and proof-of-concept microservice, designed for easy extension and experimentation. This FastAPI-based service performs common math operations, logs all requests into a SQLite database, and sends those operations to a RabbitMQ stream via CloudAMQP for further processing or async consumption.

---

## Features

- Endpoints for `power`, `factorial`, and `fibonacci` operations
- SQLite database logging of all API calls
- RabbitMQ/CloudAMQP message publishing + consumer on dev side
- Swagger UI at `/docs`
- Custom error handling (422, 500)
- Frontend UI via `index.html` + JavaScript
- Configurable input limits
- Unit-tested with `pytest`
- Docker-ready

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/math-microservice.git
cd math-microservice
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # On Unix/macOS
.venv\Scripts\activate       # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Server

```bash
uvicorn math_service.core.main:app --reload
```

Server will be available at:  
http://127.0.0.1:8000

Swagger UI:  
http://127.0.0.1:8000/docs

---

## RabbitMQ Integration 

Each successfully handled API request is also published to a RabbitMQ message queue named `math_logs`.

This allows external consumers (e.g., `consumer.py`) to asynchronously receive and process operation logs.

### Setup:

- Hosted via CloudAMQP (free plan)
- AMQP URL is stored securely in `.env` as `CLOUDAMQP_URL`
- Uses `pika` for message publishing
- Queue is declared as durable and messages are JSON-formatted

### Example Published Message:

```json
{
  "operation": "factorial",
  "input": { "n": 5 },
  "result": 120
}
```

To consume messages, run:

```bash
python math_service/core/consumer.py
```

---

## Authentication

This project currently uses a temporary session-based API key generated at runtime.

### Key Details:

- A random API key is generated at app startup
- It's displayed in the dev console (e.g., Session API Key: FKsuGRIfhJVKBSF9Yrv1nw)
- This key must be provided in requests using the `X-API-Key` header
- The frontend UI has a field where the user must paste this key

Note: This system is not production-ready and exists only for development/testing. In future versions, it can be replaced with JWT-based authentication after login support is added.

---

## Running Tests

```bash
pytest tests\test_routes.py
```

Test coverage includes:
- Valid and invalid input cases
- Security checks
- Edge case logic
- API parameter validation

---

## Docker Support

**Build:**

```bash
docker build -t math-microservice .
```

**Run:**

```bash
docker run -p 8000:8000 math-microservice
```

---

## Project Structure

```
math_service/
├── core/
│   ├── main.py                  # FastAPI app entry
│   ├── api/routes.py            # All API endpoints
│   ├── db/                      # Database init + logging
│   ├── models/schemas.py        # Pydantic models
│   ├── services/math.py         # Business logic
│   ├── utils/
│   │   ├── formatter.py         # Log formatter
│   │   ├── publisher.py         # RabbitMQ publisher (CloudAMQP)
│   ├── templates/index.html     # Frontend UI
│   └── static/                  # JS & CSS
```

---

## Authors

Developed by Octavian Cojocariu and Iulius Ambros  
For educational and learning purposes.

---

## License

This project is open-source and intended for learning. Feel free to fork and modify.
