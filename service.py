from datetime import datetime

from model.dog import Dog
from model.dog_type import DogType
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
    tmp_timestamp = Timestamp(timestamp=datetime.now())
    new_timestamp = Timestamp(id=tmp_timestamp.id,
                 timestamp=int(round(tmp_timestamp.timestamp.timestamp())))
    post_db.append(new_timestamp)
    return new_timestamp

def get_dog_by_id(id: int):
    return dogs_db.get(id)

def get_dogs_by_type(type: DogType):
    filtered_dogs = []
    for v in dogs_db.values():
        if v.kind == type:
            filtered_dogs.append(v)
    return filtered_dogs

def create_dog(dog: Dog):
    if (get_dog_by_id(dog.pk) is not None):
       return None
    
    dogs_db.pop(dog.pk, dog)
    return dog

def update_dog(dog: Dog):
    existing_dog = get_dog_by_id(dog.pk)
    if (existing_dog is None):
       return None
    dogs_db.update(dog.pk, dog)
    return dog