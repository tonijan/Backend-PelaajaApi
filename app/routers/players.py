from fastapi import APIRouter, status, Depends, HTTPException
from app.database.schemas import PlayerDb, PlayerIn, EventDb, EventIn
from app.database.database import players, save_player, fetch_player_events_by_type, fetch_player_and_events, save_event, SessionLocal
from ..database import crud
from sqlalchemy.orm import Session

router = APIRouter(prefix='/players')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#getting all players names and ids
@router.get('', response_model=list[PlayerDb], status_code=status.HTTP_200_OK)
def get_players(db: Session = Depends(get_db)):
    return crud.read_players(db)


#creating a new player
@router.post('', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerIn, db: Session = Depends(get_db)):
    return crud.create_player(db, player_in)


#getting a player by id and events
@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_player(id: int):
    return fetch_player_and_events(id)


#getting specific players events only with types
@router.get('/{id}/events', status_code=status.HTTP_200_OK)
def get_player_events(id: int, type: str = ""):
    return fetch_player_events_by_type(id, type)


#creating a new event for the player
@router.post('/{id}/events', response_model=EventDb, status_code=status.HTTP_201_CREATED)
def create_event(event_in: EventIn, id: int):
    return save_event(event_in, id)