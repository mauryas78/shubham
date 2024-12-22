from fastapi import APIRouter
from app.redis_client import get_redis_client

router = APIRouter()

@router.get("/")
async def search_books(title: str = None, author: str = None):
    redis_client = get_redis_client()
    search_key = "books:search_index"
    
    if title:
        books = redis_client.smembers(f"{search_key}:title:{title}")
    elif author:
        books = redis_client.smembers(f"{search_key}:author:{author}")
    else:
        books = redis_client.smembers(search_key)

    return {"books": list(books)}
