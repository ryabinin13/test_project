from fastapi import FastAPI
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

DATABASE_URL = "postgresql://postgres:stud@localhost:5432/library"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


from app import models, schemas
from app.routes import authors, books, borrows