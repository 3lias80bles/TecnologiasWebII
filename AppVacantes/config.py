import os

class Config:
    DEBUG = True
    PORT = 5000
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymsql://{os.getenv('DB_USER', 'root')}:"
    )
