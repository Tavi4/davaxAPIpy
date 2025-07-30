# Use official Python base image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (FastAPI default)
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "math_service.core.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
