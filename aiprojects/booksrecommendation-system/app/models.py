from pydantic import BaseModel
from typing import List

# Model for Book Recommendations Response
class Books(BaseModel):
    title : str
    author : str=''
    genre : str=''
    description : str=''


# Model for User Preferences
class User(BaseModel):
    user_password : str
    books : List[int]=[]
    recommendations : List[int]=[]

# Model for User History
# class UserHistory(BaseModel):
#     history: List[str]
