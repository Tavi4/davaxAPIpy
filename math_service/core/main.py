
from fastapi import FastAPI
from math_service.core.api.routes import router as math_router
from math_service.core.db.connection import init_db

init_db()

app = FastAPI(
    title="Math Microservice",
    description="Performs power, factorial, and fibonacci operations",
    version="1.0.0"
)


app.include_router(math_router)
