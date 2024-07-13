from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, database
from app.crud import create_short_url

router = APIRouter()


@router.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(url: schemas.URLCreate, db: Session = Depends(database.get_db)):
    short_key = create_short_url(db, url.url)
    return {"short_url": f"http://{short_key}"}
