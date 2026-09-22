from sqlalchemy.orm import sessionmaker
from app.database.database import engine

# Database Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def get_db():
    """
    FastAPI dependency for database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()