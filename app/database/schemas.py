from pydantic import BaseModel

class EventIn(BaseModel):
    type: str
    detail: str

    class Config:
        orm_mode = True


class EventDb(EventIn):
    id: int
    player_id: int
    timestamp: str


class PlayerIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PlayerDb(PlayerIn):
    id: int


class PlayerAllListItem(PlayerIn):
    id: int
    events: list[EventDb]