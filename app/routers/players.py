from fastapi import APIRouter, status, Depends, HTTPException
from app.database.models import PlayerDb, PlayerIn
from app.database.database import players, save_player, fetch_player

router = APIRouter(prefix='/players')


@router.get('', response_model=list[PlayerDb], status_code=status.HTTP_200_OK)
def get_players():
    return players


#creating a new player
@router.post('', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerIn):
    return save_player(player_in)

#getting a player by id
@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_player(id: int):
    return fetch_player(id)