from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, paginate

from database import get_session
from models import Categoria
from schemas import CategoriaCreate, CategoriaResponse

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/", response_model=Page[CategoriaResponse])
async def get_categorias(
    page: int = Query(1, ge=1),
    size: int = Query(50, ge=1, le=100),
    session: AsyncSession = Depends(get_session)
):
    result = await session.execute(select(Categoria))
    categorias = result.scalars().all()
    return paginate(categorias)

@router.post("/", response_model=CategoriaResponse)
async def create_categoria(
    categoria: CategoriaCreate,
    session: AsyncSession = Depends(get_session)
):
    nova_categoria = Categoria(**categoria.dict())
    session.add(nova_categoria)
    try:
        await session.commit()
        await session.refresh(nova_categoria)
        return nova_categoria
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Categoria já cadastrada: {categoria.nome}"
        )