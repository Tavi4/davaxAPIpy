from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from math_service.core.api.routes import router as math_router
from math_service.core.db.connection import init_db

# Initialize the database connection
init_db()

app = FastAPI(
    title="Math Microservice",
    description="Performs power, factorial, and fibonacci operations",
    version="1.0.0"
)

app.include_router(math_router)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="math_service/core/static"), name="static")
templates = Jinja2Templates(directory="math_service/core/templates")
