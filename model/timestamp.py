from pydantic import BaseModel

class Timestamp(BaseModel):
    id: int
    timestamp: int