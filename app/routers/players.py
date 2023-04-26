from fastapi import APIRouter, status, Depends, HTTPException
from app.database.models import PlayerDb, PlayerIn
from app.database.database import players, save_player

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
    index = -1
    for i, player in enumerate(players):
        if player['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="player not found", status_code=status.HTTP_404_NOT_FOUND)
    return players[index]