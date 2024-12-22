from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_book_recommendations(genre: str='',author:str='', history: list=[]):
    client = OpenAI(
    api_key=os.getenv('openai_key')
    )
    prompt = f"""
    You are an expert book reviewer and literary critic tasked with recommending 5 books.
    Based on the following user preferences and reading history, recommend 5 books that the user would likely enjoy. 

    Please provide the recommendations in a **list of JSON format**, ensuring each entry includes the title, author, genre, and a brief description of the book.

    ### Information About User Preferences ###
    - Genres: Represents the user's preferred genres, which describe the style, tone, content, literary technique, or format of the book.
    - Favorite Authors: user's favorite authors, who are creators of literary works such as novels, poems, or essays.
    - Recently Read: A JSON list of books the user has recently read, with the following structure:
    ```json
    [
        {{
        "title": "Book Title",
        "author": "Book Author",
        "genre": "Book Genre",
        "description": "Brief summary of the book"
        }}
    ]

    User Preferences:
    - Genres: {genre} 
    - Favorite Authors: {author}
    - Recently Read: {history}

    Recommend 5 books matching these preferences. Provide the title, author, and a brief description for each.
    response format:
    [{{
        "title": "Book Title",
        "author": "Book Author",
        "Genre": "Book genre"
        "description": "Brief description of the book"
    }}]
    """
    
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    store=True,
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0,
    )
    recommendations = response.choices[0].message.content
    return recommendations
