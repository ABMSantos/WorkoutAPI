# schemas.py
from pydantic import BaseModel
from typing import Optional

# --------------------
# Schemas Categoria
# --------------------
class CategoriaCreate(BaseModel):
    nome: str

class CategoriaResponse(BaseModel):
    nome: str

    class Config:
        orm_mode = True

# --------------------
# Schemas CentroTreinamento
# --------------------
class CentroTreinamentoCreate(BaseModel):
    nome: str
    endereco: str
    proprietario: str

class CentroTreinamentoResponse(BaseModel):
    nome: str
    endereco: str
    proprietario: str

    class Config:
        orm_mode = True

# --------------------
# Schemas Atleta
# --------------------
class AtletaCreate(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    categoria_id: int
    centro_treinamento_id: int

class AtletaResponse(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str

    class Config:
        orm_mode = True
