from fastapi import HTTPException
from .models import PlayerDb

players = [
    {'id': 0, 'name': 'Toni Jantunen', 'events': 'superpelaaja'},
    {'id': 1, 'name': 'Sami Dinosaurus', 'events': 'mestaripelaaja'},
    {'id': 2, 'name': 'Jaska Daniels', 'events': 'jokupelaaja'}
]


#kesken
def save_player(player_in):
    new_id = len(players)
    player = PlayerDb(**player_in.dict(), id=new_id)
    players.append(player.dict())
    return player