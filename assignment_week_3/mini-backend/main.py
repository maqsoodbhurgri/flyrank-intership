from fastapi import FastAPI
from app.routes.item_routes import router

app = FastAPI()

app.include_router(router)
