from fastapi import FastAPI
from fastapi_pagination import add_pagination
from routers.atletas import router as atletas_router
from routers.categorias import router as categorias_router
from routers.centros_treinamento import router as centros_router

from database import Base, engine

app = FastAPI(title="WorkoutAPI")

# Inclui routers
app.include_router(atletas_router)
app.include_router(categorias_router)
app.include_router(centros_router)

# Paginação global
add_pagination(app)

# Criação das tabelas no startup
@app.on_event("startup")
async def on_startup():
    # AsyncEngine precisa de contexto async para criar tabelas
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)