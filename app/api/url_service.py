from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from app import schemas, database
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import create_short_url, get_url_by_short_key

router = APIRouter()


@router.post("/shorten", response_model=schemas.URLResponse, summary="단축 URL 생성")
def shorten_url(url: schemas.URLCreate, db: Session = Depends(database.get_db)):
    short_key = create_short_url(db, url.url, url.expires_at)
    return {"short_url": f"http://{short_key}"}


@router.get("/{short_url}", summary="원본 URL 리디렉션")
def redirect_to_original_url(short_url: str, db: Session = Depends(database.get_db)):
    db_url = get_url_by_short_key(db, short_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    redirect_url = db_url.original_url
    return RedirectResponse(url=redirect_url, status_code=301)
