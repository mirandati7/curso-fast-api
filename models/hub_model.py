from sqlalchemy import Integer, String, Column
from core.configs import settings

class HubModel(settings.DBBaseModel):
    __tablename__ = 'hub'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=True)

