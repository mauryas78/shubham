from pydantic import BaseModel, validator
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

def get_unique_values(input_list):
    print(input_list)
    seen = set()
    unique_list = []
    for item in input_list:
        print(type(item))
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list