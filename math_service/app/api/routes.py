from fastapi import APIRouter, Query
from math_service.app.models.schemas import PowerRequest, PowerResponse
from math_service.app.services.math import calculate_power
from math_service.app.models.schemas import FactorialResponse
from math_service.app.services.math import calculate_factorial
from math_service.app.models.schemas import FibonacciResponse
from math_service.app.services.math import calculate_fibonacci


router = APIRouter(
    prefix="/math",
    tags=["Math Operations"]
)

@router.get("/pow", response_model=PowerResponse)
def pow_operation(base: float = Query(...), exponent: float = Query(...)):

    result = calculate_power(base, exponent)
    return PowerResponse(base=base, exponent=exponent, result=result)

@router.get("/factorial", response_model=FactorialResponse)
def factorial_operation(n: int = Query(..., ge=0)):

    result = calculate_factorial(n)
    return FactorialResponse(number=n, result=result)

@router.get("/fibonacci", response_model=FibonacciResponse)
def fibonacci_operation(n: int = Query(..., ge=0)):

    result = calculate_fibonacci(n)
    return FibonacciResponse(number=n, result=result)
