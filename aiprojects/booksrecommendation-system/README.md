# Personalized Book Recommendation API

This project is a **Personalized Book Recommendation API** that delivers intelligent and tailored book recommendations based on user preferences and reading history. It leverages OpenAI's GPT models and Redis for efficient in-memory data management, providing fast and relevant recommendations. The backend is built with a scalable, lightweight framework to ensure high performance and robustness.

## Key Features:

### Backend Development:
- **Framework**: Built with [FastAPI](https://fastapi.tiangolo.com/) for speed, data validation, and scalability.
- **Endpoints**:
  - `/user/create`: Create user with passowrd.
  - `/user/login`: Login user with passowrd.
  - `/user/preferences`: Stores or updates user preferences (e.g., genres, authors).
  - `/recommendations`: Fetches personalized book recommendations using OpenAI.
  - `/books/search`: Enables searching for books by title, author, or genre.

### Database:
- **Redis** is used for:
  - Storing user preferences and reading history.
  - Caching OpenAI-generated recommendations for faster response times
  - Indexing book metadata for efficient search operations.

### OpenAI Integration:
- **GPT-4** is used to analyze user preferences and generate book recommendations.
- Supports natural language queries for flexible and intuitive interactions.
- Customizable prompt design for accurate and creative suggestions.

### Scalable Deployment:
- Dockerized application for easy portability.
- Deployed on cloud platforms like AWS, with integrated CI/CD pipelines for continuous delivery.

### Advanced Functionalities:
- **Caching**: Optimizes API response times by caching recommendations.
- **Intelligent Query Handling**: Uses OpenAI for semantic understanding and advanced query processing.
- **Modular Codebase**: Easily extendable for future feature expansion.

## Benefits:
- Delivers a **personalized user experience** with minimal latency.
- Demonstrates modern NLP techniques and cloud deployment practices.
- Built with a **scalable, maintainable, and production-ready** architecture.

## project structure :
```plaintext
app/
├── __init__.py
├── main.py
├── redis_client.py
├── openai_service.py
├── models.py
└── endpoints/
    ├── login.py
    ├── create.py
    ├── preferences.py
    ├── recommendations.py
    └── search.py
requirements.txt
