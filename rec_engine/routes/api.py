from fastapi import APIRouter

from rest.views.organizations import router as organizations_router

router = APIRouter()

router.include_router(organizations_router)
