from fastapi import APIRouter
from app.redis_client import RedisClient,BOOKS,USER
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.authentication import authenticate
import json
router = APIRouter()

@router.get("/{title}")
async def search_books(title: str):

    redis_connection = RedisClient()
    books_dict=json.loads(redis_connection.get_value(BOOKS))
    # user_dict=json.loads(redis_connection.get_value(USER))
    print(books_dict)
    for id, book in books_dict.items():
        if book['title'] == title:
            books_dict[id]

            return {"book": books_dict[id]}
    return {'book :':'not available '}
