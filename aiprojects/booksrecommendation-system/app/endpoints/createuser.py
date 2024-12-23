from fastapi import APIRouter
from app.redis_client import RedisClient,KEY,USER
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
# from app.authentication import authenticate
from app.models import User
router = APIRouter()
import time,re , json

# import re

def is_valid_gmail(email):

    gmail_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    return bool(re.match(gmail_pattern, email))

def inallemails():
    return []

@router.get("/{email}")
async def create_user(email: str,password:str):
    try:
        redis_connection=RedisClient()
        print(email,password)
        if is_valid_gmail(email):
            user_dict=json.loads(redis_connection.get_value(USER))
            if email not in user_dict.keys():
                user_obj=User(user_password=password)
                print(user_obj)
                user_dict[email]=user_obj.dict()
                redis_connection.upsert_value(USER,json.dumps(user_dict))
                return {"message": "User created successfully ","key":KEY,"NOTE" : "add the authorization key in authorize tab on the right top corner "}
            else:
                print("already a user login")
        else:
            return {"message": "User not created .","NOTE" : "already used email OR invalid mail"}
    except Exception as e:
        print(e)
    # Store or update the user's reading history in Redis
    # redis_client.delete(f"user:{user_id}:history")  # Clear existing history
    # redis_client.rpush(f"user:{user_id}:history", *history)
    
    
