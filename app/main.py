from fastapi import FastAPI
from . import models
from .database import engine
from .api.url_service import router as api_router


models.base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)
