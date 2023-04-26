from fastapi import APIRouter, status, Depends, HTTPException
from app.database.models import EventDb, EventIn
from app.database.database import events

router = APIRouter(prefix='/events')


@router.get('', response_model=list[EventDb], status_code=status.HTTP_200_OK)
def get_events(type: str = ""):
    if type != "" and type != "level_solved" and type != "level_started":
        raise HTTPException(detail="Unknown event type", status_code=status.HTTP_400_BAD_REQUEST)
    if type == "":
        return events
    filtered_events = []
    for i, event in enumerate(events):
        if event['type'] == type:
            filtered_events.append(event)
    return filtered_events