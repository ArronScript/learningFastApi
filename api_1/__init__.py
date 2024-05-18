from fastapi import APIRouter


from .products.views import product_router

router_api_1 = APIRouter()
router_api_1.include_router(router=product_router)