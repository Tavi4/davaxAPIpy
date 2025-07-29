from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import (
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError

# Handle validation errors (e.g. missing query params)
async def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": "Invalid input", "details": exc.errors()}
    )

# Handle all uncaught exceptions
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "details": str(exc)}
    )
