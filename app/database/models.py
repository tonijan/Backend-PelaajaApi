from pydantic import BaseModel

class EventIn(BaseModel):
    type: str
    detail: str 


class EventDb(EventIn):
    id: int
    player_id: int
    timestamp: str


class PlayerIn(BaseModel):
    name: str


class PlayerDb(PlayerIn):
    id: int