from fastapi import APIRouter

from app.api.api_v1.endpoints import events

api_router = APIRouter()
api_router.include_router(events.router, prefix="", tags=["events"])
