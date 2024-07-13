from pydantic import BaseModel


class URLCreate(BaseModel):
    url: str


class URLResponse(BaseModel):
    short_url: str
