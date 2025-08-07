# Math Microservice

A learning project and proof-of-concept microservice, designed for easy extension and experimentation. This FastAPI-based service performs common math operations and logs all requests into a SQLite database. It's secured with API key authentication and includes custom error handling, Docker support, and full test coverage.

---

## Features

- Endpoints for `power`, `factorial`, and `fibonacci` operations
- SQLite database logging of all API calls
- API key authentication (`X-API-Key: secret`)
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
.venv\Scripts\activate         # On Windows
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
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Swagger UI:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


---

## Authentication

All endpoints (except `/logs` and `/`) require an API key.

**Use this header in your requests:**

```http
X-API-Key: secret
```

**Example with `curl`:**

```bash
curl -X GET "http://127.0.0.1:8000/factorial?n=5" -H "X-API-Key: secret"
```

---

## Running Tests

```bash
pytest
```

Test coverage includes:

- Valid and invalid input cases
- Security checks
- Edge case logic
- `/logs` filtering behavior

---

## Docker Support

**Build:**

```bash
docker build -t math-microservice .
```

**Run (with volume mount for SQLite DB):**

```bash
docker run -p 8000:8000 -v "${PWD}:/app" math-microservice
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
│   ├── utils/                   # Formatter, auth, etc.
│   ├── templates/index.html     # Frontend UI
│   └── static/                  # JS & CSS
```

---

## Developer Responsibilities

### Octavian Cojocariu

- Implemented all core mathematical endpoints: `/pow`, `/factorial`, `/fibonacci`
- Integrated input validation using `Query(..., ge=0, le=...)` for numeric limits
- Added global error handling for status codes `422` and `500`
- Wrote unit tests for:
  - `test_pow()`
  - `test_factorial()`
  - `test_fibonacci()`
- Introduced LRU-based caching for performance on repeated computations
- Implemented data models through Pydantic library

### Iulius Ambros

- Designed and implemented the database layer using SQLite:
  - Connection management (`connection.py`)
  - DB initialization with schema check (`init_db()`)
  - Operation logging (`log_operation`)
  - Log retrieval with filtering (`get_operation_logs`)
- Implemented the `/logs` endpoint, including limit and filtering support
- Wrote comprehensive test cases for:
  - Invalid input and edge cases (e.g., negative values, `pow(0, 0)`)
  - Log retrieval (e.g., empty results, filtered queries)
- Set up and configured `pytest` test suite
- Cleaned and validated codebase using `flake8`, and added `.flake8` config
- Built and ran Docker container for the project using Rancher Desktop
- Handled volume mounting to preserve the SQLite database across container runs

---

## License

This project is open-source and intended for learning. Feel free to fork and modify.
