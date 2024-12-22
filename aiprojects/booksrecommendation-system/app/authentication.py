from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.redis_client import KEY

# Authorization 
security = HTTPBearer()
def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials == KEY:
        return credentials
    else:
        raise HTTPException(
            status_code=401, detail="Invalid authorization code"
        )