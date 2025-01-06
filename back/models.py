from sqlalchemy import create_engine, Column, BIGINT, VARCHAR, Integer
from database import Base

class AboutMe(Base):
    __tablename__ = 'aboutme'
    id = Column(BIGINT, primary_key=True, index=True)

    text = Column(VARCHAR)

class Projects(Base):
    __tablename__ = 'projects'
    id = Column(BIGINT, primary_key=True, index=True)

    name = Column(VARCHAR)
    git = Column(VARCHAR)
    
class Ideas(Base):
    __tablename__ = 'ideas'
    id = Column(BIGINT, primary_key=True, index=True)

    name = Column(VARCHAR)
    description = Column(VARCHAR)

class Photos(Base):
    __tablename__ = 'photos'
    id = Column(BIGINT, primary_key=True, index=True)

    url = Column(VARCHAR)
    text = Column(VARCHAR)

class Memes(Base):
    __tablename__ = 'memes'
    id = Column(BIGINT, primary_key=True, index=True)

    photo = Column(VARCHAR)
    text = Column(VARCHAR)