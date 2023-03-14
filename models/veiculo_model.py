from sqlalchemy import Integer, Float, String, Column
from core.configs import settings


class VeiculoModel(settings.DBBaseModel):
    __tablename__ = 'veiculos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=True)
    cor = Column(String(100), nullable=True)
    renavam = Column(String(100), nullable=True)
    placa = Column(String(100), nullable=True)
    anoFabriccao = Column(Integer, nullable=True)
    anoModelo = Column(Integer, nullable=True)
    marca = Column(String(100), nullable=True)
    modelo = Column(String(100), nullable=True)
    versao = Column(String(100), nullable=True)
    capacidaCarga = Column(Float, nullable=True)
    categoria = Column(String(100), nullable=True)

    
    class Config:
        orm_mode = True