from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.note import Note
from app.schemas import NoteCreate, NoteResponse

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/create", response_model=NoteResponse)
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

# Get all notes present in the database
@router.get("/all", response_model=list[NoteResponse])
def get_all_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return notes

# Get notes based on the User
@router.get("/user", response_model=list[NoteResponse])
def get_notes_by_user(user_name: str, db: Session = Depends(get_db)):
    user_notes = db.query(Note).filter(Note.userName == user_name).all()
    return user_notes

# Update the Notes entry
@router.put("/update", response_model= NoteResponse)
def update_notes_by_id(id: int, update_note: NoteCreate, db: Session = Depends(get_db)):
    print(f"Updating note with id: {id}")
    updated_note = db.query(Note).filter(Note.id == id).first()

    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    updated_note.title = update_note.title
    updated_note.description = update_note.description
    updated_note.userName = update_note.userName

    db.commit()
    db.refresh(updated_note)
    return updated_note
    
