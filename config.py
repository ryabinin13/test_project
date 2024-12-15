import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:stud@localhost:5432/library"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 