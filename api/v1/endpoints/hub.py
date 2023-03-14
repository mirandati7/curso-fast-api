from fastapi import APIRouter, status, Depends, HTTPException

from typing import List
from models.hub_model import HubModel
from fastapi import status
from schemas.hub_schema import HubSchema, HubSchemaUP
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from core.deps import get_session

router = APIRouter()



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=HubSchema)
async def post_hub(hub:HubSchema, db: AsyncSession = Depends(get_session)):    
    new_hub: HubModel = HubModel(nome= hub.nome)
    
    async with db as session:
        try:
            session.add(new_hub)
            await session.commit()
            return new_hub
                
        except IntegrityError:
            raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE, detail= "Não foi possivel salvar esse hub")



@router.get('/', status_code=status.HTTP_200_OK, response_model=List[HubSchema])
async def get_hubs(db: AsyncSession = Depends(get_session)):    
    async with db as session:        
        query = select(HubModel)
        result = await session.execute(query)
        hubs: List[HubSchema] = result.scalars().unique().all()

        return hubs


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=HubSchema)
async def get_hub(id: int, db: AsyncSession = Depends(get_session)):    
    async with db as session:        
        query = select(HubModel).filter(HubModel.id == id)
        result = await session.execute(query)
        hub: HubSchema = result.scalars().unique().one_or_none()

        if hub:
            return hub
        else:
            raise HTTPException(detail="Hub não encontrado", status_code=status.HTTP_404_NOT_FOUND)    
        


@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED,response_model=HubSchema)
async def put_hub(id:int, hub: HubSchemaUP):
    if id == 1:
        hub.nome ="HUB Alterado"        
    return hub

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
async def delete_hub(id:int):
    if id == 1:
        hub = 'deletar hub'
        print(hub)  
