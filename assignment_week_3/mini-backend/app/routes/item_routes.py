from fastapi import APIRouter
from app.models.item import ItemCreate
from app.services.item_service import ItemService


router = APIRouter()

service = ItemService()


@router.post("/items")
def create_item(item: ItemCreate):
    return service.create_item(item.name)


@router.get("/items")
def get_items():
    return service.get_items()
