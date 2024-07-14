from datetime import datetime
from pydantic import BaseModel


class URLCreate(BaseModel):
    url: str
    expires_at: datetime = None


class URLResponse(BaseModel):
    short_url: str
