from datetime import timedelta
import os

class Config:
    DEBUG = True
    PORT = 5000
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )

    JWT_SECRET = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

    #Token 
    JWT_ACCESS_TOKEN_EXPIRES  = timedelta(hours = 24)
    JWT_REFRESH_TOKEN_EXPIRES  = timedelta(days = 7)