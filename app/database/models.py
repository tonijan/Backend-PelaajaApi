from pydantic import BaseModel

class EventIn(BaseModel):
    type: str
    detail: str
    player_id: int
    timestamp: str


class EventDb(EventIn):
    id: int


class PlayerIn(BaseModel):
    name: str


class PlayerDb(PlayerIn):
    id: int