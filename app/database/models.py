from pydantic import BaseModel

class PlayerIn(BaseModel):
    name: str
    events: str

class PlayerDb(PlayerIn):
    id: int