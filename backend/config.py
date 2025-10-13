import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql+psycopg://lunno:lunno@db:5432/lunno")
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-secret-change")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
    CORS_ORIGINS = [FRONTEND_URL]
