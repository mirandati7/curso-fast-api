from typing import Optional

from pydantic import BaseModel as SCBaseModel


class HubSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    
    class Config:
        orm_mode = True

class HubSchemaUP(SCBaseModel):    
    nome: str
    
    class Config:
        orm_mode = True

