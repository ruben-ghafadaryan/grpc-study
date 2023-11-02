from fastapi import APIRouter

from rest.routes import router as rest_router

router = APIRouter(prefix='/api')

router.include_router(rest_router)
