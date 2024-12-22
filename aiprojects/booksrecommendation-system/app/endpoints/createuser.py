from fastapi import APIRouter
from app.redis_client import get_redis_client
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.authentication import authenticate
router = APIRouter()

@router.post("/")
async def create_user(user_id: str, history: list,credentials: HTTPAuthorizationCredentials = Depends(authenticate)):
    redis_client = get_redis_client()
    # Store or update the user's reading history in Redis
    redis_client.delete(f"user:{user_id}:history")  # Clear existing history
    redis_client.rpush(f"user:{user_id}:history", *history)
    
    return {"message": "Reading history updated successfully."}
