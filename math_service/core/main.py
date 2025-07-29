
from fastapi import FastAPI
from math_service.core.api.routes import router as math_router
from math_service.core.db.connection import init_db

# Exceptions imports
from fastapi.exceptions import RequestValidationError
from math_service.core.utils.exceptions import (
    custom_validation_exception_handler,
    generic_exception_handler
)


init_db()

app = FastAPI(
    title="Math Microservice",
    description="Performs power, factorial, and fibonacci operations",
    version="1.0.0"
)


app.include_router(math_router)

# Register global exception handlers
app.add_exception_handler(RequestValidationError, custom_validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
