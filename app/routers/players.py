from fastapi import APIRouter, status, Depends
from app.database.schemas import PlayerDb, PlayerIn, EventDb, EventIn, PlayerAllListItem
from app.database.database import get_db
from ..database import players_crud
from sqlalchemy.orm import Session

router = APIRouter(prefix='/players')


#getting all players names and ids
@router.get('', response_model=list[PlayerDb], status_code=status.HTTP_200_OK)
def read_players(db: Session = Depends(get_db)):
    return players_crud.read_players(db)


#creating a new player
@router.post('', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerIn, db: Session = Depends(get_db)):
    return players_crud.create_player(db, player_in)


#getting a player by id and events
@router.get('/{id}', response_model=PlayerAllListItem, status_code=status.HTTP_200_OK)
def read_player_id(id: int, db: Session = Depends(get_db)):
    return players_crud.read_player_by_id(db, id)


#getting specific players events only with types
@router.get('/{id}/events', response_model=list[EventDb], status_code=status.HTTP_200_OK)
def read_player_events(id: int, type: str = "", db: Session = Depends(get_db)):
    return players_crud.read_player_events_by_type(db, id, type)


#creating a new event for the player
@router.post('/{id}/events', response_model=EventDb, status_code=status.HTTP_201_CREATED)
def create_event(event_in: EventIn, id: int, db: Session = Depends(get_db)):
    return players_crud.create_event(db, event_in, id)