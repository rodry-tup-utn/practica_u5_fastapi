from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.database import create_db_and_tables
from app.modules.health.router import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Producto Ordenes API",
    description="Sistema de Productos y Ordenes básico",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(health_router)
