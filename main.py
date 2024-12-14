from typing import Optional
from fastapi import FastAPI, status

from fastapi.responses import Response

from model.dog import Dog
import service

app = FastAPI()

@app.get('/')
def root():
    return Response(status_code = status.HTTP_200_OK)

@app.post('/')
def get_post_post():
    return service.create_timestamp()

@app.get('/dog')
def get_dogs(kind: Optional[str] = None):
    if (kind is None):
        return service.list_dogs()
    dogs = service.get_dogs_by_kind(kind)
    if len(dogs) == 0:  
        # if type not found
        return Response(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY)
    else:
        return dogs

@app.post('/dog')
def create_dogs(dog: Dog):
    created_dog = service.create_dog(dog)
    if (created_dog is None):  
        # if dog with id has already exist
        return Response(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY)
    else:
        return created_dog

@app.get('/dog/{pk}')
def get_dog_by_pk(pk: int):
    found_dog = service.get_dog_by_pk(pk)
    if found_dog is None:  
        # if dog not found
        return Response(
                status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    else:
        return found_dog

@app.patch('/dog/{pk}')
def update_dogs(pk: int, dog: Dog):
    updated_dog = service.update_dog(pk, dog)
    if (updated_dog is None):  
        # if dog with id has not exist
        return Response(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY)
    else:
        return updated_dog
