from fastapi import APIRouter
from app.api import url_service

router = APIRouter(prefix="/api")

router.include_router(url_service.router, prefix="/url", tags=["shorten"])
