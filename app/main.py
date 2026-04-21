from fastapi import FastAPI
from app.config import settings
from app.database import engine, Base
from app.controllers import notes

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    )

app.include_router(notes.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}