"""
Database connection and session management for ACC Club API
Prepared for future SQLAlchemy integration.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
from typing import Generator
from config import DATABASE_URL
import os

# For development/testing with SQLite
SQLALCHEMY_DATABASE_URL = DATABASE_URL or os.getenv(
    "DATABASE_URL",
    "sqlite:///./acc_club.db"  # Default to SQLite in project root
)

# Create engine
# For SQLite: use StaticPool to avoid threading issues
# For PostgreSQL: use default QueuePool
if "sqlite" in SQLALCHEMY_DATABASE_URL:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
else:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_pre_ping=True,
        pool_recycle=3600,
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency for FastAPI routes to get database session.
    
    Usage in routes:
    @router.get("/items")
    async def get_items(db: Session = Depends(get_db)):
        # Use db to query
        pass
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database and create tables"""
    from models import Base
    Base.metadata.create_all(bind=engine)
    print("✓ Database initialized successfully")


def reset_db():
    """Drop all tables and recreate (USE WITH CAUTION)"""
    from models import Base
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("⚠ Database reset completed. All data cleared.")


# API Connection Status Check
def check_db_connection():
    """Test database connection"""
    try:
        with engine.connect() as connection:
            print("✓ Database connection successful")
            return True
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return False


if __name__ == "__main__":
    print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")
    check_db_connection()
