from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from . import models


def read_events_by_type(db: Session, type: str):
    if type != "" and type != "level_solved" and type != "level_started":
        raise HTTPException(detail="Unknown event type", status_code=status.HTTP_400_BAD_REQUEST)
    if type == "":
        return db.query(models.Event).all()
    return db.query(models.Event).filter(models.Event.type == type).all()