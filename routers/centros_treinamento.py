from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, paginate

from database import get_session
from models import CentroTreinamento
from schemas import CentroTreinamentoCreate, CentroTreinamentoResponse

router = APIRouter(prefix="/centros", tags=["Centros de Treinamento"])

@router.get("/", response_model=Page[CentroTreinamentoResponse])
async def get_centros(
    page: int = Query(1, ge=1),
    size: int = Query(50, ge=1, le=100),
    session: AsyncSession = Depends(get_session)
):
    result = await session.execute(select(CentroTreinamento))
    centros = result.scalars().all()
    return paginate(centros)

@router.post("/", response_model=CentroTreinamentoResponse)
async def create_centro(
    centro: CentroTreinamentoCreate,
    session: AsyncSession = Depends(get_session)
):
    novo_centro = CentroTreinamento(**centro.dict())
    session.add(novo_centro)
    try:
        await session.commit()
        await session.refresh(novo_centro)
        return novo_centro
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Centro de treinamento já cadastrado: {centro.nome}"
        )