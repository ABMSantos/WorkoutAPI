from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import uuid

class Categoria(Base):
    __tablename__ = "categorias"
    pk_id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True, nullable=False)
    id = Column(String, default=lambda: str(uuid.uuid4()), unique=True)

class CentroTreinamento(Base):
    __tablename__ = "centros_treinamento"
    pk_id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True, nullable=False)
    endereco = Column(String(60), nullable=False)
    proprietario = Column(String(30), nullable=False)
    id = Column(String, default=lambda: str(uuid.uuid4()), unique=True)

class Atleta(Base):
    __tablename__ = "atletas"
    pk_id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    sexo = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.pk_id"), nullable=False)
    centro_treinamento_id = Column(Integer, ForeignKey("centros_treinamento.pk_id"), nullable=False)
    id = Column(String, default=lambda: str(uuid.uuid4()), unique=True)

    categoria = relationship("Categoria")
    centro_treinamento = relationship("CentroTreinamento")