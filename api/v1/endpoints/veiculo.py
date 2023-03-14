from typing import Optional

from pydantic import BaseModel as SCBaseModel


class VeiculoSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    cor: Optional[str]
    renavam: Optional[str]
    placa: str
    anoFabriccao: int
    anoModelo: int
    marca: str
    modelo: str
    versao: str
    capacidaCarga: float
    categoria: str

    
    class Config:
        orm_mode = True

class VeiculoSchemaUP(SCBaseModel):    
    nome: str
    cor: Optional[str]
    renavam: Optional[str]
    placa: str
    anoFabriccao: int
    anoModelo: int
    marca: str
    modelo: str
    versao: str
    capacidaCarga: float
    categoria: str
    
    class Config:
        orm_mode = True