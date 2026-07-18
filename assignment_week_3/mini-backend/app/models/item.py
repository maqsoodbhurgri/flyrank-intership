from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str


class ItemResponse(BaseModel):
    id: int
    name: str
