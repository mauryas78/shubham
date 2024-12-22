import openai

# Set your OpenAI API key here
openai.api_key = 'your-openai-api-key'

def get_book_recommendations(preferences: dict, history: list):
    prompt = f"""
    User Preferences:
    - Genres: {preferences['genres']}
    - Favorite Authors: {preferences['authors']}
    - Recently Read: {', '.join(history)}

    Recommend 5 books matching these preferences. Provide the title, author, and a brief description for each.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    recommendations = response['choices'][0]['message']['content']
    return recommendations
