from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from .database import base


class Urls(base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String(length=2000), nullable=False)
    short_key = Column(String(length=20), unique=True, index=True, nullable=False)
    expires_at = Column(DateTime, nullable=True)
    is_activate = Column(Boolean, default=True, nullable=False)
    # visit_count = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
