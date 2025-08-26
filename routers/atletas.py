from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, paginate

from database import get_session
from models import Atleta
from schemas import AtletaCreate, AtletaResponse

router = APIRouter(prefix="/atletas", tags=["Atletas"])

@router.get("/", response_model=Page[AtletaResponse])
async def get_atletas(
    nome: str | None = Query(None),
    cpf: str | None = Query(None),
    session: AsyncSession = Depends(get_session)
):
    query = select(Atleta)
    if nome:
        query = query.where(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.where(Atleta.cpf == cpf)

    result = await session.execute(query)
    atletas = result.scalars().all()
    return paginate(atletas)

@router.post("/", response_model=AtletaResponse)
async def create_atleta(
    atleta: AtletaCreate,
    session: AsyncSession = Depends(get_session)
):
    novo_atleta = Atleta(**atleta.dict())
    session.add(novo_atleta)
    try:
        await session.commit()
        await session.refresh(novo_atleta)
        return novo_atleta
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o CPF: {atleta.cpf}"
        )