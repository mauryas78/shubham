from pydantic import BaseModel
from typing import List

# Model for Book Recommendations Response
class Books(BaseModel):
    title: str
    author: str
    description: str


# Model for User Preferences
class User(BaseModel):
    AuthId: int
    books :List[Books]
    recommendations: List[Books]

# Model for User History
class UserHistory(BaseModel):
    history: List[str]
