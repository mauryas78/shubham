from fastapi import APIRouter
from app.redis_client import get_redis_client

router = APIRouter()

@router.post("/")
async def update_history(user_id: str, history: list):
    redis_client = get_redis_client()
    # Store or update the user's reading history in Redis
    redis_client.delete(f"user:{user_id}:history")  # Clear existing history
    redis_client.rpush(f"user:{user_id}:history", *history)
    
    return {"message": "Reading history updated successfully."}
