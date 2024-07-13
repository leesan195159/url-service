from sqlalchemy.orm import Session
from .models import Urls
from .utils import hash_url


def create_short_url(db: Session, original_url: str):
    existing_url = db.query(Urls).filter(Urls.original_url == original_url).first()
    if existing_url:
        return existing_url.short_key

    short_key = hash_url(original_url)

    while db.query(Urls).filter(Urls.short_key == short_key).first():
        count = 1
        short_key = hash_url(original_url + str(count))
        count += 1

    try:
        db_url = Urls(original_url=original_url, short_key=short_key)
        db.add(db_url)
        db.commit()
        return short_key
    except:
        db.rollback()
        raise


def get_url_by_short_key(db: Session, short_key: str):
    return db.query(Urls).filter(Urls.short_key == short_key).first()
