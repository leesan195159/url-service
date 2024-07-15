from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from app import schemas, database
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import create_short_url, get_url_by_short_key
from app.database import redis_client

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
    redis_client.incr(short_url)
    redirect_url = db_url.original_url
    return RedirectResponse(url=redirect_url, status_code=301)


@router.get("/stats/{short_url}", summary="통계 기능")
def get_stats(short_url: str):
    hits = redis_client.get(short_url)
    if hits is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"short_url": short_url, "hits": int(hits)}
