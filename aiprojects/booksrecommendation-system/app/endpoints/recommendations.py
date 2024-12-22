from fastapi import APIRouter
from app.redis_client import RedisClient,BOOKID,BOOKS,USER
from app.openai_service import get_book_recommendations
from app.models import Books,get_unique_values
import json
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.authentication import authenticate

router = APIRouter()

def insert_recommedations(data:list) -> list:
    try:
        print(data)
        redis_connection = RedisClient()
        recommendations_list=[]
        books_dict=json.loads(redis_connection.get_value(BOOKS))
        print(([b['title'] for b in books_dict.values()]))
        for book_detail in data:
            print("****",book_detail,"***\n")
            print((book_detail['title'] not in [b['title'] for b in books_dict.values()]))
            if book_detail['title'] not in [b['title'] for b in books_dict.values()]:
                book_id=redis_connection.get_next_id(BOOKID)
                print('----------------------------\n',book_id)
                recommendations_list.append(int(book_id))
                book_obj=Books(title=str(book_detail['title']),author=str(book_detail['author']),genre=str(book_detail['genre']),description=str(book_detail['description']))
                books_dict[str(book_id)]=book_obj.dict()
                redis_connection.upsert_value(BOOKS,json.dumps(books_dict))
            else:
                for id, book in books_dict.items():
                    if book['title'] == book_detail['title']:
                        recommendations_list.append(int(id))
        return recommendations_list
    except Exception as e:
        print('error ',e)
@router.post("/")
async def get_recommendations(email:str,genre: str='',author:str='',credentials: HTTPAuthorizationCredentials = Depends(authenticate)):
    try:
        history=[]
        book_history=[]
        redis_connection = RedisClient()
        books_dict=json.loads(redis_connection.get_value(BOOKS))
        user_dict=json.loads(redis_connection.get_value(USER))
        for i in user_dict[email]['books']:
            history.append(i)
        for i in history:
            book_history.append(books_dict[str(i)])
        # Call OpenAI for book recommendations  
        recommendations = get_book_recommendations(genre,author,book_history)
        
        # Cache the recommendations in Redis
        recommendations_ids=insert_recommedations(json.loads(recommendations)['recommendations'])
        temp_list=user_dict[email]['recommendations']+(recommendations_ids)
        re_uniquelist=get_unique_values(temp_list)
        user_dict[email]['recommendations']=re_uniquelist
        redis_connection.upsert_value(USER,json.dumps(user_dict))
    
    except Exception as e:
        print('error*',e)
    return json.loads(recommendations)
