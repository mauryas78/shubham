from fastapi import FastAPI
from app.redis_client import KEY
from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.endpoints import recommendations, preferences, createuser, search,login

app = FastAPI()
# Authorization 
security = HTTPBearer()
def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials == KEY:
        return credentials
    else:
        raise HTTPException(
            status_code=401, detail="Invalid authorization code"
        )
    
# Include routers for modularity
app.include_router(createuser.router, prefix="/user/create_user", tags=["create user"])
app.include_router(login.router, prefix="/user/login_user", tags=["login user"])
app.include_router(preferences.router, prefix="/user/preferences", tags=["Preferences"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])
app.include_router(search.router, prefix="/books/search", tags=["Search"])
