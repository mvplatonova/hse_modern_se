
from fastapi import FastAPI, status

from fastapi.responses import Response

from model.dog import Dog
from model.dog_type import DogType
import service

app = FastAPI()


@app.get('/')
def root():
    return Response(status_code = status.HTTP_200_OK)

@app.post('/')
def get_post_post():
    return Response(status_code = status.HTTP_200_OK,
                    content = service.create_timestamp())

@app.get('/dog')
def get_dogs(type: DogType):
    dogs = service.get_dogs_by_type(type)
    if len(dogs) == 0:  
        # if type not found
        return Response(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY_NOT_FOUND)
    else:
        return Response(
                status_code = status.HTTP_200_OK,
                content = dogs
        )

@app.post('/dog')
def create_dogs(dog: Dog):
    created_dog = service.create_dog(dog)
    if (created_dog is None):  
        # if dog with id has already exist
        return Response(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY_NOT_FOUND)
    else:
        return Response(
                status_code=status.HTTP_200_OK,
                content = created_dog
        )

@app.get('/dog/{id}')
def get_dog_by_pk(dog_id: int):
    found_dog = service.get_dog_by_id(dog_id)
    if found_dog is None:  
        # if dog not found
        return Response(
                status_code = status.HTTP_422_UNPROCESSABLE_ENTITY_NOT_FOUND
        )
    else:
        return Response(
                status_code = status.HTTP_200_OK, 
                content = found_dog
        )

@app.patch('/dog/{id}')
def update_dogs(dog: Dog):
    updated_dog = service.update_dog(dog)
    if (updated_dog is None):  
        # if dog with id has not exist
        return Response(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY_NOT_FOUND)
    else:
        return Response(
                status_code=status.HTTP_200_OK,
                content = updated_dog
        )