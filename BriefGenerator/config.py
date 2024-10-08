import os

class Config:
    SECRET_KEY = os.urandom(24)
    # SQLALCHEMY_DATABASE_URI = 'https://sqlalche.me/e/20/e3q8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///brief_generator.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
