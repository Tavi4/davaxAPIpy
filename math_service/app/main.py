from fastapi import FastAPI
from math_service.app.api.routes import router as math_router

app = FastAPI(
    title="Math Microservice",
    description="Performs power, factorial, and fibonacci operations",
    version="1.0.0"
)


app.include_router(math_router)
