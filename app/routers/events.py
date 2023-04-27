from fastapi import APIRouter, status, Depends, HTTPException
from app.database.models import EventDb, EventIn
from app.database.database import fetch_events_by_type

router = APIRouter(prefix='/events')


@router.get('', response_model=list[EventDb], status_code=status.HTTP_200_OK)
def get_events(type: str = ""):
    return fetch_events_by_type(type)