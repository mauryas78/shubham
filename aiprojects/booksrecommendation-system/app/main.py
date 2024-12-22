from fastapi import FastAPI
from app.endpoints import recommendations, preferences, history, search

app = FastAPI()

# Include routers for modularity
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])
app.include_router(preferences.router, prefix="/user/preferences", tags=["Preferences"])
app.include_router(history.router, prefix="/user/history", tags=["History"])
app.include_router(search.router, prefix="/books/search", tags=["Search"])
