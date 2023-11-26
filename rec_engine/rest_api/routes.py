from fastapi import APIRouter

router = APIRouter(prefix='/rest')

from rest_api.views.organizations import router as organizations_router
from rest_api.views.organizations_g import router as organizations_g_router


router.include_router(organizations_router)
router.include_router(organizations_g_router)
