from fastapi import APIRouter, status, Depends
from app.database.schemas import EventDb
from app.database.database import get_db
from ..database import events_crud
from sqlalchemy.orm import Session

router = APIRouter(prefix='/events')

#getting all events, you can filter results by type
@router.get('', response_model=list[EventDb], status_code=status.HTTP_200_OK)
def read_events(type: str = "", db: Session = Depends(get_db)):
    return events_crud.read_events_by_type(db, type)