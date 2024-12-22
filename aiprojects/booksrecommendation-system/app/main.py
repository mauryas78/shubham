from fastapi import FastAPI

from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.endpoints import recommendations, preferences, createuser, search

app = FastAPI()

# Authorization 
security = HTTPBearer()
def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials == "shubham":
        return credentials
    else:
        raise HTTPException(
            status_code=401, detail="Invalid authorization code"
        )
    
# Include routers for modularity
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])
app.include_router(preferences.router, prefix="/user/preferences", tags=["Preferences"])
app.include_router(createuser.router, prefix="/user/history", tags=["History"])
app.include_router(search.router, prefix="/books/search", tags=["Search"])
