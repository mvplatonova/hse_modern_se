from pydantic import BaseModel

from model.dog_type import DogType

class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType
