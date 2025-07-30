from fastapi import APIRouter, Query, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from math_service.core.db.logger import log_operation, get_operation_logs
from math_service.core.models.schemas import PowerResponse, FactorialResponse, FibonacciResponse
from math_service.core.services.math import (
    calculate_power, calculate_factorial, calculate_fibonacci
)
from math_service.core.utils.auth import verify_api_key
from math_service.core.utils.formatter import format_log_entry

templates = Jinja2Templates(directory="math_service/core/templates")

router = APIRouter(
    prefix="",
    tags=["Math Operations"]
)


@router.get("/pow", response_model=PowerResponse)
def pow_operation(base: float = Query(...), exponent: float = Query(...)):
    result = calculate_power(base, exponent)
    log_operation("power", {"base": base, "exponent": exponent}, result)
    return PowerResponse(base=base, exponent=exponent, result=result)


@router.get("/factorial", response_model=FactorialResponse, dependencies=[Depends(verify_api_key)])
def factorial_operation(n: int = Query(..., ge=0, le=500)):
    result = calculate_factorial(n)
    log_operation("factorial", {"n": n}, result)
    return FactorialResponse(number=n, result=result)


@router.get("/fibonacci", response_model=FibonacciResponse, dependencies=[Depends(verify_api_key)])
def fibonacci_operation(n: int = Query(..., ge=0, le=1000)):
    result = calculate_fibonacci(n)
    log_operation("fibonacci", {"n": n}, result)
    return FibonacciResponse(number=n, result=result)


@router.get("/logs")
def read_logs(limit: int = Query(10, ge=1, le=100)):
    logs = get_operation_logs(limit)
    formatted_logs = [format_log_entry(log) for log in logs]
    return {"logs": formatted_logs}


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def root_landing_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
