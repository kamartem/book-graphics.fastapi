from fastapi import APIRouter

from app.routes import exhibitions

router = APIRouter()

router.include_router(exhibitions.router, tags=["exhibitions"], prefix="/exhibitions")
