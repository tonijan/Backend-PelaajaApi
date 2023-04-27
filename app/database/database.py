from fastapi import HTTPException, status
from .models import PlayerDb, EventDb
from datetime import datetime

players = [
    {'id': 0, 'name': 'Toni Jantunen', 'events': []},
    {'id': 1, 'name': 'Sami Dinosaurus', 'events': []},
    {'id': 2, 'name': 'Jaska Daniels', 'events': []}
]

events = [
    {'id': 0, 'type': 'level_started', 'detail': 'level_666', 'timestamp': '2023-01-13 12:01:22', 'player_id': 0 },
    {'id': 1, 'type': 'level_solved', 'detail': 'level_666', 'timestamp': '2023-01-13 13:01:00', 'player_id': 0 },
    {'id': 2, 'type': 'level_started', 'detail': 'level_5', 'timestamp': '2022-01-01 10:00:50', 'player_id': 1 }
]


def save_player(player_in):
    new_id = len(players)
    player = PlayerDb(**player_in.dict(), id=new_id)
    players.append(player.dict())
    return player

def save_event(event_in, id):
    get_player_index(id)
    time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    new_id = len(events)
    event = EventDb(**event_in.dict(), id=new_id, player_id=id, timestamp=time)
    if event_in.dict()['type'] != "level_solved" and event_in.dict()['type'] != "level_started":
        raise HTTPException(detail="Unknown event type", status_code=status.HTTP_400_BAD_REQUEST)
    events.append(event.dict())
    return event



def get_player_index(id: int):
    index = -1
    for i, player in enumerate(players):
        if player['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="player not found", status_code=status.HTTP_404_NOT_FOUND)
    return index

def fetch_player(id):
    return players[get_player_index(id)]

def fetch_player_events(id):
    get_player_index(id)
    return [event for event in events if event['player_id'] == id]


def fetch_player_and_events(id):
    player = fetch_player(id)
    player['events'] = fetch_player_events(id)
    return player

def fetch_events_by_type(type):
    if type != "" and type != "level_solved" and type != "level_started":
        raise HTTPException(detail="Unknown event type", status_code=status.HTTP_400_BAD_REQUEST)
    if type == "":
        return events
    filtered_events = []
    for i, event in enumerate(events):
        if event['type'] == type:
            filtered_events.append(event)
    return filtered_events

def fetch_player_events_by_type(id, type):
    get_player_index(id)
    if type != "" and type != "level_solved" and type != "level_started":
        raise HTTPException(detail="Unknown event type", status_code=status.HTTP_400_BAD_REQUEST)
    if type == "":
        return [event for event in events if event['player_id'] == id]
    filtered_events = []
    for i, event in enumerate(events):
        if event['type'] == type and event['player_id'] == id:
            filtered_events.append(event)
    return filtered_events



