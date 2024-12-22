from fastapi import APIRouter
from app.redis_client import get_redis_client

router = APIRouter()

@router.post("/")
async def update_preferences(user_id: str, preferences: dict):
    redis_client = get_redis_client()
    # Store user preferences in Redis
    redis_client.hset(f"user:{user_id}:preferences", mapping=preferences)
    
    return {"message": "Preferences updated successfully."}
