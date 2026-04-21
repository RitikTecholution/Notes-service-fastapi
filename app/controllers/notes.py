from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.note import Note
from app.schemas import NoteCreate, NoteResponse

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(
        userName=note.userName,
        title=note.title,
        description=note.description
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note