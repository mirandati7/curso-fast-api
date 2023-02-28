from fastapi import APIRouter


from fastapi import status
from schemas.hub_schema import HubSchema, HubSchemaUP

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK)
async def get_hubs():    
    return "{'message': 'Retorna uma lista de hubs'} "


@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_hub(id: int):    
    return "{'message': 'Consultando hub'} " + str(id)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=HubSchema)
async def post_hub(hub:HubSchema):
    #hub = HubSchema(id=10, nome="HUB 01")
    return hub

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