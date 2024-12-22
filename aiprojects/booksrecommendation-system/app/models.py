from pydantic import BaseModel
from typing import List

# Model for User Preferences
class UserPreferences(BaseModel):
    genres: List[str]
    authors: List[str]

# Model for User History
class UserHistory(BaseModel):
    history: List[str]

# Model for Book Recommendations Response
class BookRecommendation(BaseModel):
    title: str
    author: str
    description: str

# Model for Book Search Request (optional if search params are passed as query params)
class BookSearchRequest(BaseModel):
    title: str = None
    author: str = None

# Model for Recommendations Response
class RecommendationsResponse(BaseModel):
    recommendations: List[BookRecommendation]
