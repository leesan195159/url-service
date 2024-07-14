import datetime

from sqlalchemy.orm import Session
from .models import Urls
from .utils import hash_url


def create_short_url(db: Session, original_url: str, expires_at: datetime.datetime = None):
    existing_url = db.query(Urls).filter(Urls.original_url == original_url, Urls.is_activate == True).first()
    if existing_url:
        return existing_url.short_key

    short_key = hash_url(original_url)
    count = 1

    while db.query(Urls).filter(Urls.short_key == short_key).first():
        short_key = hash_url(original_url + str(count))
        count += 1

    try:
        db_url = Urls(original_url=original_url, short_key=short_key, expires_at=expires_at)
        db.add(db_url)
        db.commit()
        return short_key
    except:
        db.rollback()
        raise


def get_url_by_short_key(db: Session, short_url: str):
    current_time = datetime.datetime.now()
    db_url = db.query(Urls).filter(Urls.short_key == short_url, Urls.is_activate == True).first()
    if db_url and db_url.expires_at and db_url.expires_at < current_time:
        db_url.is_activate = False
        db.commit()
        return None
    return db_url
