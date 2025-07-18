from pydantic import BaseModel

class PowerRequest(BaseModel):
    base: float
    exponent: float

class PowerResponse(BaseModel):
    base: float
    exponent: float
    result: float

# we don't need factorial request because there is only one input (number)
# it is only needed for json input type
class FactorialResponse(BaseModel):
    number: int
    result: int

class FibonacciResponse(BaseModel):
    number: int
    result: int
