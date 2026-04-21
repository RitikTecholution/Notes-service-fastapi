from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App info
    APP_NAME: str = "Todo API"
    PROJECT_NAME: str = "Todo API"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "A simple todo service built with FastAPI and SQLAlchemy."
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "sqlite:///./todo.db"

    # JWT Auth
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"  # reads from .env file

settings = Settings()