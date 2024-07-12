from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base


class Urls(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String(length=2000), nullable=False)
    short_key = Column(String(length=10), nullable=False, unique=True, index=True)
    expires_at = Column(DateTime, nullable=True)
    visit_count = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
