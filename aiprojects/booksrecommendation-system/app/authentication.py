from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# Authorization 
security = HTTPBearer()
def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials == "shubham":
        return credentials
    else:
        raise HTTPException(
            status_code=401, detail="Invalid authorization code"
        )