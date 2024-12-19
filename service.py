from datetime import datetime
import uuid

from model.dog import Dog
from model.timestamp import Timestamp

dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]

def create_timestamp() -> Timestamp:
    current_timestamp = datetime.now()
    new_timestamp = Timestamp(id=uuid.uuid4().int, timestamp=int(current_timestamp.timestamp()))
    print(new_timestamp)
    post_db.append(new_timestamp)
    return new_timestamp

def get_dog_by_pk(pk: int):
    return dogs_db.get(pk)

def get_dogs_by_kind(kind: str):
    filtered_dogs = []
    for v in dogs_db.values():
        if v.kind == kind:
            filtered_dogs.append(v)
    return filtered_dogs

def list_dogs():
    return list(dogs_db.values())

def create_dog(dog: Dog):
    if (get_dog_by_pk(dog.pk) is not None):
       return None
    dogs_db[dog.pk] = dog
    return dog

def update_dog(pk: int, dog: Dog):
    existing_dog = dogs_db.pop(pk, None)
    if (existing_dog is None):
       return None
    dogs_db[dog.pk] = dog
    return dog
