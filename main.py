from fastapi import FastAPI
from fastapi_pagination import add_pagination
from routers.atletas import router as atletas_router
from routers.categorias import router as categorias_router
from routers.centros_treinamento import router as centros_router

from database import Base, engine
import asyncio

app = FastAPI(title="WorkoutAPI")

app.include_router(atletas_router, prefix="/atletas", tags=["Atletas"])
app.include_router(categorias_router, prefix="/categorias", tags=["Categorias"])
app.include_router(centros_router, prefix="/centros", tags=["Centros de Treinamento"])

add_pagination(app)

# Cria as tabelas automaticamente (para desenvolvimento)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Inicializa o banco antes de subir o servidor
@app.on_event("startup")
async def on_startup():
    await init_models()
