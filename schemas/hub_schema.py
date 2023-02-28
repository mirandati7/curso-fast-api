from typing import Optional

from pydantic import BaseModel as SCBaseModel


class HubSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    endereco:str
    

    class Config:
        orm_mode = False

class HubSchemaUP(SCBaseModel):    
    nome: str
    endereco:str
    

    class Config:
        orm_mode = False

