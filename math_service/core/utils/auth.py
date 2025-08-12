# Proof of concept, authentification not fully implemented
from fastapi import Header, HTTPException, status
import secrets

SESSION_API_KEY = secrets.token_urlsafe(16)
print(f" Session API Key: {SESSION_API_KEY}")


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != SESSION_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
