from fastapi import APIRouter, status, Depends, HTTPException
from app.database.models import PlayerDb, PlayerIn
from app.database.database import players, save_player, fetch_player_events_by_type, fetch_player_and_events

router = APIRouter(prefix='/players')

#getting all players names and ids
@router.get('', response_model=list[PlayerDb], status_code=status.HTTP_200_OK)
def get_players():
    return players


#creating a new player
@router.post('', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerIn):
    return save_player(player_in)


#getting a player by id and events
@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_player(id: int):
    return fetch_player_and_events(id)


#getting specific players events only with types
@router.get('/{id}/events', status_code=status.HTTP_200_OK)
def get_player_events(id: int, type: str = ""):
    return fetch_player_events_by_type(id, type)