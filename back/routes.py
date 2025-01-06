from fastapi import APIRouter, Depends
from database import get_db, Session
from models import *

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the my API!"}

@router.get("/aboutme")
async def hui(db: Session = Depends(get_db)):
    return db.query(AboutMe).all()

@router.put("/aboutme")
async def hui(info: str, db: Session = Depends(get_db)):
    aboutme = db.query(AboutMe).filter(AboutMe.id == 1).first()
    aboutme.text = info
    db.commit()
    return {aboutme.id: aboutme.text}