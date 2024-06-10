from fastapi import APIRouter


from .products.views import product_router
from .security.views import security_router

router_api_1 = APIRouter()
router_api_1.include_router(router=product_router)
router_api_1.include_router(router=security_router)