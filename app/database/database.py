from fastapi import HTTPException, status
from .models import PlayerDb, EventDb

players = [
    {'id': 0, 'name': 'Toni Jantunen'},
    {'id': 1, 'name': 'Sami Dinosaurus'},
    {'id': 2, 'name': 'Jaska Daniels'}
]

events = [
    {'id': 0, 'type': 'level_started', 'detail': 'level_666', 'timestamp': '2023-01-13 12:01:22', 'player_id': 0 },
    {'id': 1, 'type': 'level_solved', 'detail': 'level_666', 'timestamp': '2023-01-13 13:01:00', 'player_id': 0 },
    {'id': 2, 'type': 'level_started', 'detail': 'level_5', 'timestamp': '2022-01-01 10:00:50', 'player_id': 1 }
]


#kesken
def save_player(player_in):
    new_id = len(players)
    player = PlayerDb(**player_in.dict(), id=new_id)
    players.append(player.dict())
    return player


def fetch_player(id):
    return players[get_player_index(id)]


def get_player_index(id: int):
    index = -1
    for i, player in enumerate(players):
        if player['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="player not found", status_code=status.HTTP_404_NOT_FOUND)
    return index

