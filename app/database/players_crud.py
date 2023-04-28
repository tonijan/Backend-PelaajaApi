from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def read_players(db: Session):
    return db.query(models.Player).all()

def create_player(db: Session, player_in: schemas.PlayerIn):
    player = models.Player(**player_in.dict())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def read_player_by_id(db: Session, id: int):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(detail="player not found", status_code=status.HTTP_404_NOT_FOUND)
    return player

def read_player_events_by_type(db: Session, id: int, type: str):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(detail="player not found", status_code=status.HTTP_404_NOT_FOUND)
    if type != "" and type != "level_solved" and type != "level_started":
        raise HTTPException(detail="Unknown event type", status_code=status.HTTP_400_BAD_REQUEST)
    if type == "":
        return db.query(models.Event).filter(models.Event.player_id == id).all()
    return db.query(models.Event).filter(models.Event.player_id == id).filter(models.Event.type == type).all()
    

def create_event(db:Session, event_in: schemas.EventIn, id: int):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(detail="player not found", status_code=status.HTTP_404_NOT_FOUND)
    if event_in.dict()['type'] != "level_solved" and event_in.dict()['type'] != "level_started":
        raise HTTPException(detail="Unknown event type", status_code=status.HTTP_400_BAD_REQUEST)
    time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    event = models.Event(**event_in.dict(), player_id = id, timestamp = time)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event
