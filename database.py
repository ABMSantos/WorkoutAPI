from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Substitua com suas credenciais
DATABASE_URL = "postgresql+asyncpg://usuario:senha@localhost:5432/workoutapi"

# Cria engine assíncrona
engine = create_async_engine(DATABASE_URL, echo=True)

# Sessão assíncrona
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base declarativa
Base = declarative_base()

# Dependência para injeção em rotas
async def get_session() -> AsyncSession: # type: ignore
    async with AsyncSessionLocal() as session:
        yield session