from fastapi import APIRouter
from app.redis_client import get_redis_client
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.authentication import authenticate
router = APIRouter()

@router.get("/{title}")
async def search_books(title: str):
    search_key = "books:search_index"
    
    if title:
        books = redis_client.smembers(f"{search_key}:title:{title}")

    return {"books": list(books)}
