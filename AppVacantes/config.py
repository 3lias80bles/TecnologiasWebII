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

    SQLALCHEMY_TRACK_MODIFICATIONS = False  

    # Configuración JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Clave secreta para firmar tokens
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
