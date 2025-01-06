from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the API!"}

@router.get("/hui")
async def root():
    return {"message": "Welcome to the hui!"}