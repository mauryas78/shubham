from fastapi import APIRouter
from app.redis_client import get_redis_client
from app.openai_service import get_book_recommendations

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.authentication import authenticate

router = APIRouter()

@router.post("/")
async def get_recommendations(user_id: str,credentials: HTTPAuthorizationCredentials = Depends(authenticate)):
    # Fetch preferences and history from Redis
    redis_client = get_redis_client()
    preferences = redis_client.hgetall(f"user:{user_id}:preferences")
    history = redis_client.lrange(f"user:{user_id}:history", 0, -1)

    if not preferences or not history:
        return {"error": "User preferences or history not found."}

    # Call OpenAI for book recommendations
    recommendations = get_book_recommendations(preferences, history)
    
    # Cache the recommendations in Redis
    redis_client.set(f"recommendations:{user_id}", recommendations)

    return {"recommendations": recommendations}
