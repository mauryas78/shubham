from fastapi import APIRouter
from app.redis_client import RedisClient,BOOKS,USER,BOOKID
from app.models import Books
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.authentication import authenticate
import json
router = APIRouter()

@router.post("/")
async def update_preferences(email: str, title: str,author: str='',genre:str='',credentials: HTTPAuthorizationCredentials = Depends(authenticate)):
    try:
        redis_connection = RedisClient()
        books_dict=json.loads(redis_connection.get_value(BOOKS))
        user_dict=json.loads(redis_connection.get_value(USER))
        if title not in [b['title'] for b in books_dict.values()]:
            book_id=redis_connection.get_next_id(BOOKID)
            book_obj=Books(title=title,author=author,genre=genre)
            books_dict[book_id]=book_obj.dict()
            redis_connection.upsert_value(BOOKS,json.dumps(books_dict))
            user_dict[email]['books'].append(book_id)
            redis_connection.upsert_value(USER,json.dumps(user_dict))

        else:
            for id, book in books_dict.items():
                if book['title'] == title:
                    user_dict[email]['books'].append(int(id))
                    redis_connection.upsert_value(USER,json.dumps(user_dict))

        return{"message":"successfully added the book preferences"}
    except Exception as e:
        print(e)



    

    

    # # Store user preferences in Redis
    # redis_client.hset(f"user:{user_id}:preferences", mapping=preferences)
    
    # return {"message": "Preferences updated successfully."}
data ={"books" : {
    '2': {'title': 'test1', 'author': '', 'genre': '', 'description': ''},
    '5': {'title': 'ram ram', 'author': '', 'genre': '', 'description': ''},
    '6':{ 'title': 'book three', 'author': '', 'genre': '', 'description': ''}
}}