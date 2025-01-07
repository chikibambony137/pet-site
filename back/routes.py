from fastapi import APIRouter, Depends
from database import get_db, Session
from models import *

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the my API!"}



@router.get("/aboutme")
async def get_aboutme(db: Session = Depends(get_db)):
    return db.query(AboutMe).first()

@router.put("/aboutme")
async def update_aboutme(info: str, db: Session = Depends(get_db)):
    aboutme = db.query(AboutMe).filter(AboutMe.id == 1).first()
    aboutme.text = info
    db.commit()
    return {aboutme.id: aboutme.text}



@router.get("/projects")
async def get_projects(db: Session = Depends(get_db)):
    return db.query(Projects).all()

@router.post("/projects/add")
async def add_projects(Name: str, Git: str, db: Session = Depends(get_db)):
    new_project = Projects(name=Name, git=Git)
    db.add(new_project)
    db.commit()
    return {new_project.id: new_project.name}

@router.put("/projects/update")
async def update_project(Id: int, Name: str, Git: str, db: Session = Depends(get_db)):
    try:
        project = db.query(Projects).filter(Projects.id == Id).first()
        project.name = Name
        project.git = Git
        db.commit()
        return {project.id: project.name}
    except:
        return {"Id not found": Id}
    
@router.delete("/projects/delete")
async def delete_project(Id: int, db: Session = Depends(get_db)):
    try:
        project = db.query(Projects).filter(Projects.id == Id).first()
        db.delete(project)
        db.commit()
        return {project.id: project.name}
    except:
        return {"Id not found": Id}
    


@router.get("/ideas")
async def get_ideas(db: Session = Depends(get_db)):
    return db.query(Ideas).all()

@router.post("/ideas/add")
async def add_idea(Name: str, Description: str, db: Session = Depends(get_db)):
    new_idea = Ideas(name=Name, description=Description)
    db.add(new_idea)
    db.commit()
    return {new_idea.id: new_idea.name}

@router.put("/ideas/update")
async def update_idea(Id: int, Name: str, Description: str, db: Session = Depends(get_db)):
    try:
        idea = db.query(Ideas).filter(Ideas.id == Id).first()
        idea.name = Name
        idea.description = Description
        db.commit()
        return {idea.id: idea.name}
    except:
        return {"Id not found": Id}
    
@router.delete("/ideas/delete")
async def delete_idea(Id: int, db: Session = Depends(get_db)):
    try:
        idea = db.query(Ideas).filter(Ideas.id == Id).first()
        db.delete(idea)
        db.commit()
        return {idea.id: idea.name}
    except:
        return {"Id not found": Id}
    


@router.get("/photos")
async def get_photos(db: Session = Depends(get_db)):
    return db.query(Photos).all()

@router.post("/photos/add")
async def add_photo(Url: str, Text: str, db: Session = Depends(get_db)):
    new_photo = Photos(url=Url, text=Text)
    db.add(new_photo)
    db.commit()
    return {new_photo.id: new_photo.url}

@router.put("/photos/update")
async def update_photo(Id: int, Url: str, Text: str, db: Session = Depends(get_db)):
    try:
        photo = db.query(Photos).filter(Photos.id == Id).first()
        photo.url = Url
        photo.text = Text
        db.commit()
        return {photo.id: photo.url}
    except:
        return {"Id not found": Id}
    
@router.delete("/photos/delete")
async def delete_photo(Id: int, db: Session = Depends(get_db)):
    try:
        photo = db.query(Photos).filter(Photos.id == Id).first()
        db.delete(photo)
        db.commit()
        return {photo.id: photo.url}
    except:
        return {"Id not found": Id}
    


@router.get("/memes")
async def get_memes(db: Session = Depends(get_db)):
    return db.query(Memes).all()

@router.post("/memes/add")
async def add_memes(Photo: str, Text: str, db: Session = Depends(get_db)):
    new_meme = Memes(photo=Photo, text=Text)
    db.add(new_meme)
    db.commit()
    return {new_meme.id: new_meme.photo}

@router.put("/memes/update")
async def update_photo(Id: int, Photo: str, Text: str, db: Session = Depends(get_db)):
    try:
        meme = db.query(Memes).filter(Memes.id == Id).first()
        meme.photo = Photo
        meme.text = Text
        db.commit()
        return {meme.id: meme.photo}
    except:
        return {"Id not found": Id}
    
@router.delete("/memes/delete")
async def delete_meme(Id: int, db: Session = Depends(get_db)):
    try:
        meme = db.query(Memes).filter(Memes.id == Id).first()
        db.delete(meme)
        db.commit()
        return {meme.id: meme.photo}
    except:
        return {"Id not found": Id}