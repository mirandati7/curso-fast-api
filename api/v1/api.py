from fastapi import APIRouter

from api.v1.endpoints import hub

api_router = APIRouter()

api_router.include_router(hub.router, prefix='/hubs', tags=['hubs'])
